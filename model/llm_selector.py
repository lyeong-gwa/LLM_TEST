import os
from dotenv import load_dotenv

def get_llm():
    # 1. 서버 전역 .env 로드 (파일이 없어도 에러 발생하지 않음)
    if os.path.exists(".env"):
        load_dotenv(dotenv_path=".env")

    # 2. LLM_PROVIDER 결정
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    # 3. model/{provider}.env 로드
    provider_env_path = f"model/{provider}.env"
    if os.path.exists(provider_env_path):
        load_dotenv(dotenv_path=provider_env_path, override=True)

    # 4. LLM 객체 생성 (최신 langchain-openai 방식)
    if provider == "azure":
        from langchain_openai import AzureChatOpenAI
        return AzureChatOpenAI(
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            model=os.getenv("AZURE_OPENAI_MODEL", "gpt-4o"),
            temperature=0.7,
        )
    else:
        from langchain_openai import ChatOpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        model = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
        
        # API 키 검증
        if not api_key:
            raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다. model/openai.env 파일을 확인해주세요.")
        
        return ChatOpenAI(
            api_key=api_key,
            model=model,
            temperature=0.7,
        ) 