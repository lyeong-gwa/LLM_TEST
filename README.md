# CEYES - AI 챗봇 및 코드 어시스턴트

CEYES는 Streamlit을 기반으로 한 AI 챗봇 및 코드 어시스턴트 애플리케이션입니다. OpenAI와 Azure OpenAI를 지원하며, 사용자 정의 프롬프트 관리 시스템을 제공합니다.

## 🚀 주요 기능

- **AI 챗봇**: 대화형 AI 어시스턴트
- **코드 어시스턴트**: 코드 작성 및 수정 도움
- **프롬프트 관리**: 모듈화된 프롬프트 시스템
- **다중 LLM 지원**: OpenAI 및 Azure OpenAI
- **Streamlit UI**: 사용자 친화적인 웹 인터페이스

## 📁 프로젝트 구조

```
내가만든ceyes - 2/
├── app.py                          # 메인 애플리케이션 진입점
├── requirements.txt                # Python 의존성
├── config/                         # 설정 파일
│   ├── config.py                   # 기본 설정
│   └── data/
│       └── rules_list.json         # 규칙 데이터
├── model/                          # LLM 모델 관련
│   ├── llm_selector.py             # LLM 선택기
│   ├── openai.env                  # OpenAI 환경 변수
│   └── azure.env                   # Azure OpenAI 환경 변수
├── prompt/                         # 프롬프트 관리
│   ├── chatbot_prompt_manager.py   # 챗봇 프롬프트 관리자
│   ├── code_assistant_prompt_manager.py  # 코드 어시스턴트 프롬프트 관리자
│   ├── chatbot_prompts/            # 챗봇 프롬프트
│   │   ├── chatbot_main.md
│   │   └── chatbot_ask.md
│   └── code_assistant_prompts/     # 코드 어시스턴트 프롬프트
│       └── code_assistant.md
├── ui/                             # 사용자 인터페이스
│   ├── streamlit_ui.py             # 메인 Streamlit UI
│   ├── chatbot_ui.py               # 챗봇 UI 컴포넌트
│   └── codefix_ui.py               # 코드 수정 UI 컴포넌트
├── chain/                          # LangChain 체인 (예정)
└── tools/                          # 도구 모음 (예정)
```

## 🛠️ 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 환경 변수 설정

#### OpenAI 사용 시
`model/openai.env` 파일을 생성하고 다음 내용을 추가하세요:

```
OPENAI_API_KEY=your_openai_api_key_here
```

#### Azure OpenAI 사용 시
`model/azure.env` 파일을 생성하고 다음 내용을 추가하세요:

```
AZURE_OPENAI_API_KEY=your_azure_openai_api_key_here
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint_here
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

### 3. 애플리케이션 실행

```bash
streamlit run app.py
```

## 🔧 설정

### LLM 선택
`model/llm_selector.py`에서 사용할 LLM을 선택할 수 있습니다.

### 프롬프트 커스터마이징
- `prompt/chatbot_prompts/`: 챗봇 프롬프트 수정
- `prompt/code_assistant_prompts/`: 코드 어시스턴트 프롬프트 수정

### 규칙 데이터
`config/data/rules_list.json`에서 애플리케이션 규칙을 관리할 수 있습니다.

## 📝 사용법

1. 애플리케이션을 실행하면 Streamlit 웹 인터페이스가 열립니다
2. 챗봇 탭에서 일반적인 대화를 할 수 있습니다
3. 코드 어시스턴트 탭에서 코드 작성 및 수정 도움을 받을 수 있습니다

## 🤝 기여

프로젝트에 기여하고 싶으시다면:

1. 이 저장소를 포크하세요
2. 새로운 기능 브랜치를 생성하세요 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋하세요 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시하세요 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성하세요

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## ⚠️ 주의사항

- API 키는 절대 공개 저장소에 커밋하지 마세요
- `.env` 파일은 `.gitignore`에 포함되어 있습니다
<<<<<<< HEAD
- 프로덕션 환경에서는 적절한 보안 조치를 취하세요 
=======
- 프로덕션 환경에서는 적절한 보안 조치를 취하세요 
>>>>>>> 75f13a7c52be93387e79f3d20dca827804c830f2
