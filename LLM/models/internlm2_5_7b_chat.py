"""
author:
description:

"""
import os
import sys
sys.path.append("/root/Project_FunGPT/FunGPT/")
import copy
import warnings
from typing import Callable, List, Optional

import streamlit as st
import torch
from torch import nn
from transformers.generation.utils import (LogitsProcessorList,
                                           StoppingCriteriaList)
from transformers.utils import logging

from transformers import AutoTokenizer, AutoModelForCausalLM
from Utils.model_settings import GenerationConfig
logger = logging.get_logger(__name__)


from Utils.configs import Config


class InternLM:
    def __init__(self, mode='offline', model_path = 'THUDM/chatglm3-6b'):
        self.mode = mode
        self.model, self.tokenizer = self.init_model(model_path)
        self.history = None
        assert self.mode == 'offline', "InternLM只支持离线模式"

    def init_model(self, model_path):
        model = AutoModelForCausalLM.from_pretrained(model_path, 
                                                     device_map="auto", 
                                                     trust_remote_code=True).eval()
        tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
        return model, tokenizer
    
    # 流式输出
    @torch.inference_mode()
    def generate(
        self, 
        prompt,
        generation_config: Optional[GenerationConfig] = None,
        logits_processor: Optional[LogitsProcessorList] = None,
        stopping_criteria: Optional[StoppingCriteriaList] = None,
        prefix_allowed_tokens_fn: Optional[Callable[[int, torch.Tensor],
                                                    List[int]]] = None,
        additional_eos_token_id: Optional[int] = None,
        **kwargs,
    ):
        
        inputs = self.tokenizer([prompt], padding=True, return_tensors='pt')
        input_length = len(inputs['input_ids'][0])
        for k, v in inputs.items():
            inputs[k] = v.cuda()
        input_ids = inputs['input_ids']
        _, input_ids_seq_length = input_ids.shape[0], input_ids.shape[-1]

        if generation_config is None:
            generation_config = self.model.generation_config

        generation_config = copy.deepcopy(generation_config)
        model_kwargs = generation_config.update(**kwargs)
        bos_token_id, eos_token_id = (  # noqa: F841  # pylint: disable=W0612
            generation_config.bos_token_id,
            generation_config.eos_token_id,
        )
        if isinstance(eos_token_id, int):
            eos_token_id = [eos_token_id]
        if additional_eos_token_id is not None:
            eos_token_id.append(additional_eos_token_id)
        has_default_max_length = kwargs.get(
            'max_length') is None and generation_config.max_length is not None
        if has_default_max_length and generation_config.max_new_tokens is None:
            warnings.warn(
                f"Using 'max_length''s default \
                    ({repr(generation_config.max_length)}) \
                    to control the generation length. "
                'This behaviour is deprecated and will be removed from the \
                    config in v5 of Transformers -- we'
                ' recommend using `max_new_tokens` to control the maximum \
                    length of the generation.',
                UserWarning,
            )
        elif generation_config.max_new_tokens is not None:
            generation_config.max_length = generation_config.max_new_tokens + \
                input_ids_seq_length
            if not has_default_max_length:
                logger.warn(  # pylint: disable=W4902
                    f"Both 'max_new_tokens' (={generation_config.max_new_tokens}) "
                    f"and 'max_length'(={generation_config.max_length}) seem to "
                    "have been set. 'max_new_tokens' will take precedence. "
                    'Please refer to the documentation for more information. '
                    '(https://huggingface.co/docs/transformers/main/'
                    'en/main_classes/text_generation)',
                    UserWarning,
                )

        if input_ids_seq_length >= generation_config.max_length:
            input_ids_string = 'input_ids'
            logger.warning(
                f'Input length of {input_ids_string} is {input_ids_seq_length}, '
                f"but 'max_length' is set to {generation_config.max_length}. "
                'This can lead to unexpected behavior. You should consider'
                " increasing 'max_new_tokens'.")

        # 2. Set generation parameters if not already defined
        logits_processor = logits_processor if logits_processor is not None \
            else LogitsProcessorList()
        stopping_criteria = stopping_criteria if stopping_criteria is not None \
            else StoppingCriteriaList()

        logits_processor = self.model._get_logits_processor(
            generation_config=generation_config,
            input_ids_seq_length=input_ids_seq_length,
            encoder_input_ids=input_ids,
            prefix_allowed_tokens_fn=prefix_allowed_tokens_fn,
            logits_processor=logits_processor,
        )

        stopping_criteria = self.model._get_stopping_criteria(
            generation_config=generation_config,
            stopping_criteria=stopping_criteria)
        logits_warper = self.model._get_logits_warper(generation_config)

        unfinished_sequences = input_ids.new(input_ids.shape[0]).fill_(1)
        scores = None
        while True:
            model_inputs = self.model.prepare_inputs_for_generation(
                input_ids, **model_kwargs)
            # forward pass to get next token
            outputs = self.model(
                **model_inputs,
                return_dict=True,
                output_attentions=False,
                output_hidden_states=False,
            )

            next_token_logits = outputs.logits[:, -1, :]

            # pre-process distribution
            next_token_scores = logits_processor(input_ids, next_token_logits)
            next_token_scores = logits_warper(input_ids, next_token_scores)

            # sample
            probs = nn.functional.softmax(next_token_scores, dim=-1)
            if generation_config.do_sample:
                next_tokens = torch.multinomial(probs, num_samples=1).squeeze(1)
            else:
                next_tokens = torch.argmax(probs, dim=-1)

            # update generated ids, model inputs, and length for next step
            input_ids = torch.cat([input_ids, next_tokens[:, None]], dim=-1)
            model_kwargs = self.model._update_model_kwargs_for_generation(
                outputs, model_kwargs, is_encoder_decoder=False)
            unfinished_sequences = unfinished_sequences.mul(
                (min(next_tokens != i for i in eos_token_id)).long())

            output_token_ids = input_ids[0].cpu().tolist()
            output_token_ids = output_token_ids[input_length:]
            for each_eos_token_id in eos_token_id:
                if output_token_ids[-1] == each_eos_token_id:
                    output_token_ids = output_token_ids[:-1]
            response = self.tokenizer.decode(output_token_ids)

            yield response
            # stop when each sentence is finished
            # or if we exceed the maximum length
            if unfinished_sequences.max() == 0 or stopping_criteria(
                    input_ids, scores):
                break

    # def generate(self, prompt, system_prompt=""):  # system_prompt这个后面统一写
    #     # 把system_prompt加进去
    #     # if self.history == None:
    #     #     self.history = [system_prompt]

    #     # try:
    #     response, self.history = self.model.chat(self.tokenizer, prompt, history=self.history)
    #     return response
    #     # except Exception as e:
    #     #     print(e)
    #     #     return "对不起，请稍后再次尝试。"

    def chat(self, system_prompt, message):
        response = self.generate(message, system_prompt)
        self.history.append((message, response))
        return response, self.history

    def clear_history(self):
        self.history = []


def test():
    llm = InternLM(mode='offline',model_path=Config.PROJECT_PATH / 'LLM/weights/internlm2_5-1_8b-chat')
    answer = llm.generate("请介绍一下你自己")
    print(answer)

if __name__ == '__main__':
    test()