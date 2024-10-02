import streamlit as st

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
        st.rerun()

def get_avatar(identifier):
    # Function to fetch avatars
    return f"/root/Project_FunGPT/Developing/Assets/avatar/{identifier}.png"

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
