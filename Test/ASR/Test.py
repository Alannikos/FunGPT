import streamlit as st
from audio_recorder_streamlit import audio_recorder

input_type = st.radio("选择输入方式:", ("文字", "语音"))