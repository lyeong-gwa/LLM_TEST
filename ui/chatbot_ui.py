import streamlit as st


def chatbot_ui(llm, chatbot_prompt, prompt_key=None):
    with st.expander("💬 챗봇 테스트", expanded=True):
        st.markdown("""
        <div style='padding: 1.5rem 1rem; background: linear-gradient(90deg, #B2FEFA 0%, #0ED2F7 100%); border-radius: 0.75rem;'>
          <h2 style='color: #222; font-size: 1.7rem; margin-bottom: 0.5rem;'>💬 Chatbot 테스트</h2>
          <p style='color: #333; font-size: 1.1rem;'>OpenAI LLM과 자유롭게 대화해보세요.</p>
        </div>
        """, unsafe_allow_html=True)
        st.divider()
        if "chatbot_messages" not in st.session_state:
            st.session_state.chatbot_messages = [
                {"role": "system", "content": chatbot_prompt.get_prompt().replace("{SESSION_INFO}", "")},
                {"role": "assistant", "content": "안녕하세요. 소스코드검증 챗봇입니다. 무엇을 도와드릴까요?"}
            ]
            
        for msg in st.session_state.chatbot_messages[1:]:
            st.chat_message(msg["role"]).write(msg["content"])
        user_input = st.chat_input("메시지를 입력하세요...")
        if user_input:
            st.session_state.chatbot_messages.append({"role": "user", "content": user_input})
            st.session_state.chatbot_messages.append({"role": "assistant", "content": "답변 생성 중..."})
            st.rerun()

        # 답변 생성 중이면 LLM 호출
        if (
            len(st.session_state.chatbot_messages) > 1
            and st.session_state.chatbot_messages[-1]["role"] == "assistant"
            and st.session_state.chatbot_messages[-1]["content"] == "답변 생성 중..."
        ):
            response = llm.invoke(st.session_state.chatbot_messages[:-1])
            print(st.session_state.chatbot_messages[:-1])
            st.session_state.chatbot_messages[-1]["content"] = response.content
            st.rerun()