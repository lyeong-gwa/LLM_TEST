import streamlit as st
from streamlit_ace import st_ace
import json
import os
from prompt.chatbot_prompt_manager import ChatbotPromptManager
from prompt.code_assistant_prompt_manager import CodeAssistantPromptManager
from ui.codefix_ui import codefix_ui
from ui.chatbot_ui import chatbot_ui

def sidebar():
    if st.sidebar.button("🛠 코드수정지원", use_container_width=True):
        st.session_state.menu = "codefix"
    if st.sidebar.button("💬 챗봇 테스트", use_container_width=True):
        st.session_state.menu = "chatbot"
def header():
    st.markdown("""
    <style>
    @keyframes wave {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }
    .wave-header {
      animation: wave 8s ease-in-out infinite;
      background: linear-gradient(270deg, #EEAECA, #94BBE9);
      background-size: 400% 400%;
      padding: 1.5rem 1rem;
      border-radius: 0.75rem;
    }
    .wave-header h1 {
      color: white;
      font-size: 2.2rem;
      margin-bottom: 0.5rem;
    }
    .wave-header p {
      color: #f0f0f0;
      font-size: 1.1rem;
    }
    </style>
    <div class='wave-header'>
      <h1>⌨️ CodeEyes Assistant</h1>
      <p>💡 SonarQube 룰 기반 코드 품질 분석 및 수정 코드 제안을 도와드립니다.</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
def init_session(system_prompt):
    if "messages" not in st.session_state:
        st.session_state.followup_response = ""
        st.session_state.messages = [{"role": "system", "content": system_prompt}]

def main_ui(llm, chatbot_prompt_manager: ChatbotPromptManager, code_assistant_prompt_manager: CodeAssistantPromptManager, rule_list_func):
    st.set_page_config(page_title="CodeEyes Assistant", layout="wide")
    sidebar()
    header()
    menu = st.session_state.get("menu", "codefix")
    if menu == "codefix":
        prompt = code_assistant_prompt_manager.get_prompt()
        codefix_ui(llm, prompt, rule_list_func)
    elif menu == "chatbot":
        prompt = chatbot_prompt_manager
        chatbot_ui(llm, prompt)
