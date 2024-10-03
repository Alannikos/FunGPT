import streamlit as st
import requests


user_prompt = '<|im_start|>user\n{user}<|im_end|>\n'
robot_prompt = '<|im_start|>assistant\n{robot}<|im_end|>\n'
cur_query_prompt = '<|im_start|>user\n{user}<|im_end|>\n\
    <|im_start|>assistant\n'

def initialize_session_state():
    if "LLM_Model" not in st.session_state:
        st.session_state.LLM_Model = None
    if "ASR_Model" not in st.session_state:
        st.session_state.ASR_Model = None
    if "TTS_Model" not in st.session_state:
        st.session_state.TTS_Model = None
        
    if "llm_config" not in st.session_state:
        st.session_state.llm_config = None
    if "asr_config" not in st.session_state:
        st.session_state.asr_config = None
    if "tts_config" not in st.session_state:
        st.session_state.tts_config = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.sidebar.button("是否清空对话"):
        st.session_state.chat_history = []
        # st.rerun()

def combine_history(prompt):
    messages = st.session_state.chat_history
    meta_instruction = ('You are InternLM (书生·浦语), a helpful, honest, '
                    'and harmless AI assistant developed by Shanghai '
                    'AI Laboratory (上海人工智能实验室).')

    total_prompt = f'<s><|im_start|>system\n{meta_instruction}<|im_end|>\n'
    for message in messages:
        cur_content = message['content']
        if message['role'] == 'user':
            cur_prompt = user_prompt.format(user=cur_content)
        elif message['role'] == 'robot':
            cur_prompt = robot_prompt.format(robot=cur_content)
        else:
            raise RuntimeError
        total_prompt += cur_prompt
    total_prompt = total_prompt + cur_query_prompt.format(user=prompt)
    return total_prompt

def initialize_session_state_p2():
    if "LLM_Model_p2" not in st.session_state:
        st.session_state.LLM_Model_p2 = None
    if "ASR_Model_p2" not in st.session_state:
        st.session_state.ASR_Model_p2 = None
    if "TTS_Model_p2" not in st.session_state:
        st.session_state.TTS_Model_p2 = None

    if "llm_config_p2" not in st.session_state:
        st.session_state.llm_config_p2 = None
    if "asr_config_p2" not in st.session_state:
        st.session_state.asr_config_p2 = None
    if "tts_config_p2" not in st.session_state:
        st.session_state.tts_config_p2 = None
    if "chat_history_p2" not in st.session_state:
        st.session_state.chat_history_p2 = []

    if st.sidebar.button("是否清空对话"):
        st.session_state.chat_history_p2 = []
        st.rerun()

def combine_history_p2(prompt):
    messages = st.session_state.chat_history_p2
    meta_instruction = ('You are InternLM (书生·浦语), a helpful, honest, '
                    'and harmless AI assistant developed by Shanghai '
                    'AI Laboratory (上海人工智能实验室).')

    total_prompt = f'<s><|im_start|>system\n{meta_instruction}<|im_end|>\n'
    for message in messages:
        cur_content = message['content']
        if message['role'] == 'user':
            cur_prompt = user_prompt.format(user=cur_content)
        elif message['role'] == 'robot':
            cur_prompt = robot_prompt.format(robot=cur_content)
        else:
            raise RuntimeError
        total_prompt += cur_prompt
    total_prompt = total_prompt + cur_query_prompt.format(user=prompt)
    return total_prompt

def get_avatar(identifier):
    # 返回头像
    return f"/root/Project_FunGPT/Developing/Assets/avatar/{identifier}.png"

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()