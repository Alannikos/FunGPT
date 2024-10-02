import os
import sys
sys.path.append("/root/Project_FunGPT/Developing")

from ASR.models.sensevoice import Sensevoice
from TTS.models.chattts import MyChatTTS
from LLM.models.internlm2_5_7b_chat import InternLM

def init_LLM_Model(model_path, mode=None):
    if mode == None:
        return InternLM(model_path=model_path)
    else:
        return InternLM(mode=mode, model_path=model_path)
    
def init_TTS_Model(model_path):
    return MyChatTTS(model_path=model_path)

def init_ASR_Model(model_path):
    return Sensevoice(model_path=model_path)
