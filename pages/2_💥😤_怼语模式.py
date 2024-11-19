import os
import gc
import sys
import time
import torch
import requests
from dataclasses import asdict
import streamlit as st
from streamlit_lottie import st_lottie
sys.path.append("/root/Project_FunGPT/Developing")

from Utils.model_utils import init_LLM_Model, init_ASR_Model, init_TTS_Model
from Utils.model_settings import llm_settings, asr_settings, tts_settings
from Utils.common_utils import initialize_session_state
from Utils.common_utils import get_avatar, combine_history, load_lottieurl
from Utils.data_utils import get_audio_input, handle_user_input
from Utils.configs import Config

def main():
    st.title("FunGPT  -  您的情感调酒师🍹")

    # 加载动画
    lottie_cocktail = load_lottieurl("https://lottie.host/159ecdad-0271-4e38-9549-7a6d92d2faf3/VrZHqb1c1G.json")

    # 创建两列布局
    col1, col2 = st.columns([1, 1])  # 左右列比例均等

    with col1:
        st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
        st_lottie(lottie_cocktail, height=250, width=250, key="cocktail")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        # 添加空白实现对齐
        st.markdown("<div style='height:37px;'></div>", unsafe_allow_html=True)
        st.info("💥 别自欺欺人了，直面现实吧！")
        st.warning("⚔️ 你的借口听起来就像泡沫，一戳就破！")
        st.error("💢 你的想法太天真，现实可不是童话书！")

    # 在文本和分隔线之间的空白
    st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

    # 添加动画分隔线
    st.markdown("""
        <style>
        .animated-line {
            width: 100%;
            height: 2px;
            background: linear-gradient(to right, #ff7f50, #87cefa);
            animation: slideIn 2s ease-in-out infinite alternate;
        }
        @keyframes slideIn {
            from {
                width: 0%;
            }
            to {
                width: 100%;
            }
        }
        </style>
        <div class='animated-line'></div>
    """, unsafe_allow_html=True)

    # 全局样式优化：保持卡片样式一致
    st.markdown("""
        <style>
        .stInfo, .stSuccess, .stWarning {
            margin-bottom: 10px;
            border-radius: 10px;
        }
        </style>
        """, unsafe_allow_html=True)

    st.sidebar.title("模型设置")

    initialize_session_state()

    llm_config = llm_settings()
    asr_config = asr_settings()
    tts_config = tts_settings()

    loading_placeholder = st.sidebar.empty()

    # 当模型不需要使用时，删除模型
    if not llm_config["use"] and st.session_state.LLM_Model is not None:
        del st.session_state.LLM_Model
        del st.session_state.llm_config
        gc.collect()
        torch.cuda.empty_cache()
        time.sleep(1)

    if not asr_config["use"] and st.session_state.ASR_Model is not None:
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

    # 初始化模型
    if llm_config["use"] and (st.session_state.LLM_Model is None or st.session_state.llm_config != llm_config):
        loading_placeholder.info("正在加载LLM模型...")
        st.session_state.LLM_Model = init_LLM_Model(model_path=Config.PROJECT_PATH / 'LLM/weights/internlm2_5-7b-chat')

        st.session_state.llm_config = llm_config
        loading_placeholder.success("LLM模型加载完成！")
        time.sleep(1)
        loading_placeholder.empty()

    if asr_config["use"] and (st.session_state.ASR_Model is None or st.session_state.asr_config != asr_config):
        loading_placeholder.info("正在加载ASR模型...")
        # time.sleep(2)
        st.session_state.ASR_Model = init_ASR_Model(Config.PROJECT_PATH / "ASR/weights/SenseVoiceSmall")
        st.session_state.asr_config = asr_config
        loading_placeholder.success("ASR模型加载完成！")
        time.sleep(1)
        loading_placeholder.empty()

    if tts_config["use"] and (st.session_state.TTS_Model is None or st.session_state.tts_config != tts_config):
        loading_placeholder.info("正在加载TTS模型...")
        st.session_state.tts_config = tts_config
        st.session_state.TTS_Model = init_TTS_Model(Config.PROJECT_PATH / 'TTS/weights/ChatTTS', st.session_state.tts_config['voice'])
        loading_placeholder.success("TTS模型加载完成！")
        time.sleep(1)
        loading_placeholder.empty()

    # 展示历史对话
    for message in st.session_state.chat_history:
        with st.chat_message(message['role'], avatar=get_avatar("User_v1" if message['role'] == 'user' else "BanterBot")):
            st.markdown(message['content'])
            if 'wav_path' in message and message['wav_path'] is not None:
                # 展示之前的语音输入结果
                st.session_state.TTS_Model.show_audio(message['wav_path'])

    # 处理用户的输入(两个维度：语音以及文本)
    handle_user_input(mode=2)

if __name__ == "__main__":
    main()