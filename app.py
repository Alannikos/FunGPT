import os
import sys
import streamlit as st

def sidebar_content():

    st.sidebar.markdown("### 欢迎关注")

    st.sidebar.markdown("""
    <style>
    .sidebar-link {
        display: inline-flex;
        align-items: center;
        margin: 0px 10px 10px 0px;
        padding: 5px 10px;
        text-decoration: none;
        border-radius: 5px;
        border: 1px solid #ddd;
        color: #000; /* 黑色文字 */
        background-color: #ffcc00; /* 黄色背景 */
    }
    .sidebar-link:hover {
        background-color: #e6b800; /* 深黄色 */
    }
    .sidebar-link img {
        width: 20px;
        height: 20px;
        margin-right: 5px;
    }
    </style>
    
    <a href="https://github.com/Alannikos" target="_blank" class="sidebar-link">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@13.7.0/icons/github.svg" alt="GitHub"> GitHub
    </a>
    <a href="https://space.bilibili.com/3494365446015137" target="_blank" class="sidebar-link">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@13.7.0/icons/bilibili.svg" alt="Bilibili"> Bilibili
    </a>
    <a href="https://huggingface.co/" target="_blank" class="sidebar-link">
        <img src="https://cdn.jsdelivr.net/npm/simple-icons@13.7.0/icons/huggingface.svg" alt="Hugging Face"> Hugging Face
    </a>
    """, unsafe_allow_html=True)
    
    # 在侧边栏底部添加内容
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 关于我们")
    st.sidebar.markdown("FunGPT --- 智能情感调酒师")
    st.sidebar.markdown("© 2024 FunGPT Team")
    st.sidebar.markdown("[联系我们](#) | [使用条款](#)")

def main():
    st.set_page_config(
        page_title="FunGPT App",
        page_icon="🧊",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )
    st.title("FunGPT  -  您的情感调酒师🍹")

    sidebar_content()

if __name__ == '__main__':
    main()