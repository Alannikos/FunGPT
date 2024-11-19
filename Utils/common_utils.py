import sys
import requests
import streamlit as st
import jieba
import pickle
from flashtext import KeywordProcessor

sys.path.append("/root/Project_FunGPT/FunGPT/")

from LLM.templates.template import Template
from Utils.configs import Config

user_prompt = '<|im_start|>user\n{user}<|im_end|>\n'
robot_prompt = '<|im_start|>assistant\n{robot}<|im_end|>\n'
cur_query_prompt = '<|im_start|>user\n{user}<|im_end|>\n\
    <|im_start|>assistant\n'


class SecureSystem:
    """
    敏感词检测模块
    """

    def __init__(self):
        self.sensitive_path = Config.PROJECT_PATH / "Data/BanterBot/sensitive_words/sensitive_words.pkl"

        # 加载词库
        self.load_words()

    def load_words(self):
        with open(self.sensitive_path, 'rb') as f:
            sensitive_words = pickle.load(f)

        self.sensitive_words = sensitive_words

    def tokenize(self, text):
        """
        对输入进行分词
        """
        tokenized_text = " ".join(jieba.cut(text))
        return tokenized_text

    def check(self, text):
        """
        进行检测
        """

        tokenized_text = self.tokenize(text)

        processor = KeywordProcessor()
        processor.add_keywords_from_list(self.sensitive_words)
        isContain = len(processor.extract_keywords(tokenized_text)) > 0
        return isContain

def initialize_session_state():
    if "SecureSystem" not in st.session_state:
        st.session_state.SecureSystem = SecureSystem()

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
    # meta_instruction = ('You are InternLM (书生·浦语), a helpful, honest, '
    #                 'and harmless AI assistant developed by Shanghai '
    #                 'AI Laboratory (上海人工智能实验室).')
    meta_instruction = (Template.KUA_GENERATE_DATA_TEMPLATE)

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
    if "SecureSystem" not in st.session_state:
        st.session_state.SecureSystem = SecureSystem()
        
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
    messages = st.session_state.chat_history
    # meta_instruction = ('You are InternLM (书生·浦语), a helpful, honest, '
    #                 'and harmless AI assistant developed by Shanghai '
    #                 'AI Laboratory (上海人工智能实验室).')
    meta_instruction = (Template.DUI_GENERATE_DATA_TEMPLATE)

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
    return f"{Config.PROJECT_PATH}" + "Assets/avatar/{identifier}.jpg"

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
