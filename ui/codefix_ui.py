import streamlit as st
from streamlit_ace import st_ace

def codefix_ui(llm, system_prompt, rule_list_func, prompt_key=None):
    with st.expander("🛠 코드수정지원 정보 입력", expanded=True):
        col_lang, col_rule = st.columns([1, 3])
        with col_lang:
            language = st.selectbox("언어", ["Python", "Java", "JavaScript"], index=0)
            language = language.lower()
        with col_rule:
            rule_list = rule_list_func(language)
            rule_titles = [f"{r['title']}" for r in rule_list]
            selected_rule = st.selectbox("룰 선택 (입력 시 자동 검색)", options=rule_titles)
        rulename = selected_rule.split(" - ")[0] if selected_rule else ""
        st.markdown("**🔤 분석할 코드를 입력하세요:**")
        dark_mode = st.toggle("🌙 에디터 다크 모드", value=True)
        theme = "dracula" if dark_mode else "github"
        code = st_ace(language=language.lower(), theme=theme, height=300, key="ace_input", auto_update=True)
        analyze_button = st.button("🚀 Analyze", use_container_width=True, disabled=not (rulename.strip() and code and code.strip()))
        if analyze_button:
            st.session_state.followup_response = ""
            with st.spinner("분석 중입니다..."):
                st.session_state.messages.append({
                    "role": "user",
                    "content": f"language: {language}\nrulename: {rulename}\ncode:\n{code}"
                })
                result_markdown = llm.invoke(st.session_state.messages)
                st.session_state.analysis_result = result_markdown
    if "analysis_result" in st.session_state:
        st.markdown("---")
        st.markdown("#### 📊 분석 결과")
        st.code(st.session_state.analysis_result)