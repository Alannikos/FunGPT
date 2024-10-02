import os
import sys
import time
import torch
from dataclasses import asdict
import streamlit as st
from audio_recorder_streamlit import audio_recorder

sys.path.append("/root/Project_FunGPT/Developing")
from Utils.common_utils import get_avatar, combine_history

# def get_audio_input():

#     translating_placeholder = st.empty()
#     # 记录音频
#     audio_file = audio_recorder("Record", key="record")

#     # 如果录制了音频，则进行转换
#     if audio_file:
#         try:
#             user_wav_path = st.session_state.ASR_Model.save_wavs(audio_file)
#             return st.session_state.ASR_Model.generate(user_wav_path)
#         except:
#             translating_placeholder.info("ASR模型未加载或加载失败...")
#             time.sleep(2)
#             translating_placeholder.empty()

# def get_audio_input():
#     with st.sidebar:
#         st.title("语音输入")
#         # 创建三列布局
#         col1, col2, col3 = st.columns([1, 2, 1])
#         translating_placeholder = st.empty()

#         # 在第一列放置录音按钮
#         with col1:
#             audio_file = audio_recorder('', key="record")

#         # 在第二列放置文本显示区域
#         with col2:
#             text_placeholder = st.empty()

#         # 在第三列放置发送按钮
#         with col3:
#             send_button = st.button("发送", key="send_button", disabled=False)

#         # 如果录制了音频，则进行转换
#         if audio_file:
#             try:
#                 user_wav_path = st.session_state.ASR_Model.save_wavs(audio_file)
#                 transcribed_text = st.session_state.ASR_Model.generate(user_wav_path)
                
#                 # 显示转换后的文本
#                 text_placeholder.text_area("转换结果:", value=transcribed_text, height=100, key="transcribed_text")
                
#                 # 返回转换后的文本，但不立即发送
#                 if send_button:
#                     text_placeholder.empty()
#                     return transcribed_text
#                 else:
#                     return None
#                 # return transcribed_text if send_button else None

#             except:
#                 translating_placeholder.info("ASR模型未加载或加载失败...")
#                 time.sleep(2)
#                 translating_placeholder.empty()

#     return None

def get_audio_input():
    with st.sidebar:
        st.markdown("---")
        st.title("语音输入")
        translating_placeholder = st.empty()

        # 第一行：录音按钮
        with st.container():
            st.markdown("#### 录音区域")
            audio_file = audio_recorder('🌟', key="record")
            st.markdown("---")
        
        # 第二行：文本显示区域
        with st.container():
            st.markdown("#### 📝 转换结果")
            text_placeholder = st.empty()
            edited_text = st.session_state.get('edited_text', "")  # 用于编辑后的文本
            st.markdown("---")

        # 第三行：发送按钮
        with st.container():
            st.markdown("#### ✉️ 发送")
            send_button = st.button("📬 发送", key="send_button")
            # st.markdown("---")

        # 如果录制了音频，则进行转换
        if audio_file:
            translating_placeholder = st.empty()
            try:
                user_wav_path = st.session_state.ASR_Model.save_wavs(audio_file)
                transcribed_text = st.session_state.ASR_Model.generate(user_wav_path)
                
                # 显示并允许用户编辑转换后的文本
                edited_text = text_placeholder.text_area(
                    label="识别后文字", 
                    value=transcribed_text,
                    height=100,
                    key="transcribed_text"
                )

                # 保存编辑后的文本
                st.session_state.edited_text = edited_text

                # 返回编辑后的文本
                if send_button:
                    return edited_text
                else:
                    return None

            except Exception as e:
                translating_placeholder.info("❗ ASR模型未加载或加载失败...")
                time.sleep(2)
                translating_placeholder.empty()

    return None

def handle_user_input():
    user_input = None
    input_type = None

    # 尝试获取语音输入
    audio_input = get_audio_input()
    if audio_input:
        user_input = audio_input
        input_type = "audio"
    
    # 如果没有语音输入,尝试获取文字输入
    if not user_input:
        text_input = st.chat_input('欢迎和我交流o~')
        if text_input:
            user_input = text_input
            input_type = "text"
    
    # 如果有用户输入,处理它
    if user_input:
        with st.chat_message('user', avatar=get_avatar("person2")):
            st.markdown(user_input)
        
        new_history = combine_history(user_input)
        st.session_state.chat_history.append({'role': 'user', 'content': user_input})

        model_placeholder = st.empty()
        try:
            wav_path = None
            with st.chat_message('robot', avatar=get_avatar("person1")):
                message_placeholder = st.empty()
                for cur_response in st.session_state.LLM_Model.generate(new_history, **asdict(st.session_state.llm_config['config'])):
                    message_placeholder.markdown(cur_response)
                
                if st.session_state.tts_config['use']:
                    with st.spinner():
                        wav_path = st.session_state.TTS_Model.generate(cur_response, speed=st.session_state.tts_config['speed'])
                        st.session_state.TTS_Model.show_audio(wav_path)

            st.session_state.chat_history.append({'role': 'robot', 'content': cur_response, 'wav_path': wav_path})
            torch.cuda.empty_cache()
        except Exception as e:
            model_placeholder.info("❗存在模型未加载或加载失败...")
            time.sleep(2)
            model_placeholder.empty()