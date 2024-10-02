import os
import gc
import sys
import time
import torch
from dataclasses import asdict
import streamlit as st
sys.path.append("/root/Project_FunGPT/Developing")

from Utils.model_utils import init_LLM_Model, init_ASR_Model, init_TTS_Model
from Utils.model_settings import llm_settings, asr_settings, tts_settings
from Utils.common_utils import initialize_session_state
from Utils.common_utils import get_avatar, combine_history
from Utils.data_utils import get_audio_input, handle_user_input

def main():
    st.title("FunGPT --- 您的智能情感调酒师🍹")

    st.sidebar.title("模型设置")

    initialize_session_state()

    llm_config = llm_settings()
    asr_config = asr_settings()
    tts_config = tts_settings()

    loading_placeholder = st.sidebar.empty()

    # 当模型不需要使用时，删除模型或设为 None
    if not llm_config["use"] and st.session_state.LLM_Model is not None:
        # st.session_state.LLM_Model = None
        # st.session_state.llm_config = None
        del st.session_state.LLM_Model
        del st.session_state.llm_config
        gc.collect()
        torch.cuda.empty_cache()
        time.sleep(1)

    if not asr_config["use"] and st.session_state.ASR_Model is not None:
        # st.session_state.ASR_Model = None
        # st.session_state.asr_config = None
        del st.session_state.ASR_Model
        del st.session_state.asr_config
        gc.collect()
        torch.cuda.empty_cache()
        time.sleep(1)

    if not tts_config["use"] and st.session_state.TTS_Model is not None:
        del st.session_state.TTS_Model
        del st.session_state.tts_config
        gc.collect()
        torch.cuda.empty_cache()
        time.sleep(1)

    if llm_config["use"] and (st.session_state.LLM_Model is None or st.session_state.llm_config != llm_config):
        loading_placeholder.info("正在加载LLM模型...")
        st.session_state.LLM_Model = init_LLM_Model(model_path='/root/Project_FunGPT/Developing/LLM/weights/internlm2_5-1_8b-chat')
        st.session_state.llm_config = llm_config
        loading_placeholder.success("LLM模型加载完成！")
        time.sleep(1)
        loading_placeholder.empty()

    if asr_config["use"] and (st.session_state.ASR_Model is None or st.session_state.asr_config != asr_config):
        loading_placeholder.info("正在加载ASR模型...")
        # time.sleep(2)
        st.session_state.ASR_Model = init_ASR_Model("/root/Project_FunGPT/Developing/ASR/weights/SenseVoiceSmall")
        st.session_state.asr_config = asr_config
        loading_placeholder.success("ASR模型加载完成！")
        time.sleep(1)
        loading_placeholder.empty()

    if tts_config["use"] and (st.session_state.TTS_Model is None or st.session_state.tts_config != tts_config):
        loading_placeholder.info("正在加载TTS模型...")
        st.session_state.TTS_Model = init_TTS_Model('/root/Project_FunGPT/Developing/TTS/weights/ChatTTS')
        st.session_state.tts_config = tts_config
        loading_placeholder.success("TTS模型加载完成！")
        time.sleep(1)
        loading_placeholder.empty()

    # 展示历史对话
    for message in st.session_state.chat_history:
        with st.chat_message(message['role'], avatar=get_avatar("person2" if message['role'] == 'user' else "person1")):
            st.markdown(message['content'])
            if 'wav_path' in message:
                # 展示之前的语音输入结果
                st.session_state.TTS_Model.show_audio(message['wav_path'])

    handle_user_input()

if __name__ == "__main__":
    main()