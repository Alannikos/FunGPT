import streamlit as st
from dataclasses import asdict, dataclass

@dataclass
class GenerationConfig:
    max_length: int = 32768
    top_p: float = 0.8
    temperature: float = 0.8
    do_sample: bool = True
    repetition_penalty: float = 1.005


def llm_settings():
    st.sidebar.subheader("LLM 设置")
    use_llm = st.sidebar.checkbox("启用语言模型 (LLM)", value=False)
    if use_llm:
        max_length = st.sidebar.slider('Max Length',
                               min_value=8,
                               max_value=32768,
                               value=32768)
        top_p = st.sidebar.slider('Top P', 0.0, 1.0, 0.8, step=0.01)
        temperature = st.sidebar.slider('Temperature', 0.0, 1.0, 0.7, step=0.01)

        generation_config = GenerationConfig(max_length=max_length,
                                            top_p=top_p,
                                            temperature=temperature)

        return {"use": use_llm, "config": generation_config}

    return {"use": False}

def asr_settings():
    st.sidebar.subheader("ASR 设置")
    use_asr = st.sidebar.checkbox("启用语音识别 (ASR)", value=False)
    if use_asr:
        language = st.sidebar.selectbox("识别语言", ["自动检测", "英文", "中文"])
        return {"use": use_asr, "language": language}
    return {"use": False}

def tts_settings():
    st.sidebar.subheader("TTS 设置")
    use_tts = st.sidebar.checkbox("启用文本转语音 (TTS)", value=False)
    if use_tts:
        voice = st.sidebar.selectbox("选择音色", ["默认", "女声1", "男声1", "女声2"])
        speed = st.sidebar.slider("语速", 3, 7, 5, 1)
        return {"use": use_tts, "voice": voice, "speed": speed}
    return {"use": False}

