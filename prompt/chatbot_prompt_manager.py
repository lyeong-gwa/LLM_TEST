import os
from prompt.prompt import load_prompt

class ChatbotPromptManager:
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        self.main_prompt = load_prompt(os.path.join(base_dir, "chatbot_prompts", "chatbot_main.md"))
        self.ask_prompt = load_prompt(os.path.join(base_dir, "chatbot_prompts", "chatbot_main.md"))
        # 필요시 여러 프롬프트를 dict 등으로 관리 가능

    def get_prompt(self, key=None):
        # key에 따라 분기된 프롬프트 반환 (확장 가능)
        if key=='ask':
            return self.ask_prompt
        return self.main_prompt 