사용자의 정보를 요약한 json 데이터를 받았다.

Input데이터 양식은 다음과 같다.
{
  "session_info" : {
    "user_info" : "",
    "service_name" : "부하발생기",
    "service_code" : ""
  },
  "q_type" : "serviceinfo_q"
}

Input 데이터 설명
json 객체의 1 depth attr은 "session_info", "q_type" 이 주어진다.
session_info는 이후 답변을 내리기위해 파악한 정보들이 구성된다.
q_type은 질문유형이다.

### 세션변수
사용자 질문에서 확인할 수 없는 정보는 ""로 저장한다.
- **user_info** : 질문중인 사용자 정보
- **service_name** : 질의대상이 되는 서비스명
- **service_code** : 서비스의 도메인 (4가지 종류: `ITO`, `SM`, `SI`, `Dspace`)

### 사용자 질문유형
질의간 비슷한 유형이 있을 수 있다. 이런 경우 가급적 가까운 유형으로 판단하라
- **process_q** :  
  소스코드검증 서비스 자체의 프로세스에 대한 질의  
  _예시: ITO서비스 수용방법 등_
- **auth_q** :  
  서비스 접근권한 변경(추가, 제거, PM권한수정)
  _예시: 82273957 사용자를 OG0704서비스에 권한추가 요청 등_
- **serviceinfo_q** :  
  등록된 서비스의 정보 일부 수정 요청  
  _예시: 형상의 브랜치 변경 등_
- **other_q** :  
  어느 유형인지 판단이 되지 않는 경우