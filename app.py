from model.llm_selector import get_llm
from ui.streamlit_ui import main_ui
from config.config import load_rule_list
from prompt.chatbot_prompt_manager import ChatbotPromptManager
from prompt.code_assistant_prompt_manager import CodeAssistantPromptManager
# 룰 리스트 함수 래퍼
def rule_list_func(language):
    return load_rule_list(language)

llm = get_llm()
chatbot_prompt_manager = ChatbotPromptManager()
code_assistant_prompt_manager = CodeAssistantPromptManager()

main_ui(llm, chatbot_prompt_manager, code_assistant_prompt_manager, rule_list_func)