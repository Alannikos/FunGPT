import io
import re
import numpy as np
import soundfile as sf
from pathlib import Path
from pydub import AudioSegment
from datetime import datetime
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
from audio_recorder_streamlit import audio_recorder


class Sensevoice:
    def __init__(self, model_path):
        self.load_model(model_path)

    def load_model(self, model_path):
        self.model = AutoModel(model=model_path,
                        vad_model="fsmn-vad",
                        vad_kwargs={"max_single_segment_time": 30000},
                        trust_remote_code=True, device="cuda:0")

    def save_wavs(self, wav_bytes):
        save_file = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".wav"
        wav_save_path = str(Path("./Work_dirs/ASR").joinpath(save_file).absolute())
        
        audio_segment = AudioSegment.from_wav(io.BytesIO(wav_bytes))
        audio_segment.export(wav_save_path, format='wav')
        # wav_bytes.export(wav_save_path, format="wav")

        return wav_save_path

    # 调用模型生成文字
    def generate(self, wav_path):
        texts = self.model.generate(
                            input=wav_path,
                            cache={},
                            language="auto", # "zn", "en", "yue", "ja", "ko", "nospeech"
                            use_itn=False,
                            batch_size_s=0,
        )

        new_text = re.sub("<.*?>", "", texts[0]["text"])
        return new_text
    
    # def record_voice(self):

if __name__ == "__main__":
    model_path = "/root/Project_FunGPT/Developing/ASR/weights/SenseVoiceSmall"
    model = Sensevoice(model_path=model_path)
    print(model.generate('/root/Project_FunGPT/Developing/Data/ASR/aaa.wav'))