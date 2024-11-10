# Import necessary libraries and configure settings
import sys
sys.path.append('/root/Project_FunGPT/FunGPT/')
import os
import torch
import torchaudio
import numpy as np
import soundfile as sf
from pathlib import Path
from datetime import datetime
# from TTS_Model import ChatTTS  #type:ignore
import ChatTTS
torch._dynamo.config.cache_size_limit = 64
torch._dynamo.config.suppress_errors = True
torch.set_float32_matmul_precision('high')
import lzma
import numpy as np
import pybase16384 as b14

import streamlit as st

from Utils.configs import Config


class MyChatTTS:
    def __init__(self, model_path, speaker_type=None):
        self.load_model(model_path=model_path)
        """
        有时间用map优化一下，这里处理的有点丑陋
        """
        if (speaker_type == None or speaker_type == "默认"):
            self.speaker = self.compress_and_encode(torch.load(Config.PROJECT_PATH / 'TTS/weights/Speaker/seed_1089_restored_emb.pt', map_location=torch.device('cpu')).detach())
        elif (speaker_type == "温柔女声"):
            self.speaker = self.compress_and_encode(torch.load(Config.PROJECT_PATH / 'TTS/weights/Speaker/wenrou_girl.pt', map_location=torch.device('cpu')).detach())
        elif (speaker_type == "活泼女声"):
            self.speaker = self.compress_and_encode(torch.load(Config.PROJECT_PATH / 'TTS/weights/Speaker/active_girl.pt', map_location=torch.device('cpu')).detach())
        elif (speaker_type == "清秀男声"):
            self.speaker = self.compress_and_encode(torch.load(Config.PROJECT_PATH / 'TTS/weights/Speaker/active_boy.pt', map_location=torch.device('cpu')).detach())
        elif (speaker_type == "磁性男声"):
            self.speaker = self.compress_and_encode(torch.load(Config.PROJECT_PATH / 'TTS/weights/Speaker/cixing_boy.pt', map_location=torch.device('cpu')).detach())
        else:
            self.speaker = self.compress_and_encode(torch.load(Config.PROJECT_PATH / 'TTS/weights/Speaker/seed_742_restored_emb.pt', map_location=torch.device('cpu')).detach())

    def compress_and_encode(self, tensor):
        np_array = tensor.numpy().astype(np.float16)
        compressed = lzma.compress(np_array.tobytes(), format=lzma.FORMAT_RAW,
                                filters=[{"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME}])
        encoded = b14.encode_to_string(compressed)
        return encoded

    def load_model(self, model_path):
        """
        初始化模型
        """
        self.chat = ChatTTS.Chat()
        self.chat.load(compile=False, source='custom', custom_path=model_path)  # 用这个最新的配置

    def generate(self, text, speed=5, oral=3, laugh=3, bk=3):
        """
        参数说明：\n
            1. text: 文本\n
            2. oral: 口语\n
            3. laugh: 笑声\n
            4. bk: 停顿\n
            5. wav_save_path: 音频文件保存地址
        """

        # 句子全局设置：讲话人音色和速度
        params_infer_code = ChatTTS.Chat.InferCodeParams(
            prompt=f"speed_{speed}",
            spk_emb=self.speaker, # 声音模型
        )

        """
        得到音频文件
        type: list[array()]
        """
        wavs = self.chat.infer(
            text,
            params_infer_code=params_infer_code,
        )

        save_file = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".wav"
        wav_save_path = str(Path(Config.PROJECT_PATH / "Work_dirs/TTS").joinpath(save_file).absolute())
        self.save_wavs(wavs, wav_save_path)
        
        return wav_save_path

    # 保存音频文件
    def save_wavs(self, wav, wav_save_path):
        """
        参数说明：\n
            1. wav: 声音文件
            2. wav_save_path: 音频文件保存地址

        """
        wav_data = np.array(wav[0])
        sf.write(wav_save_path, np.ravel(wav_data), samplerate=24000)

    # 展示音频文件
    def show_audio(self, wav_save_path, sample_rate=24000):
        if wav_save_path is None:
            return
        # 读入音频
        st.audio(wav_save_path, format="audio/wav")

if __name__ == "__main__":
    text = "哈哈哈"

    model = MyChatTTS(model_path=Config.PROJECT_PATH / 'TTS/weights/ChatTTS')
    model.generate(text)

