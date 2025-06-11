# 🌸 PiBoo: 성분부터 궁합까지, 똑똑한 화장품 도우미

# 👥 팀 소개
> SK네트웍스 Family AI 캠프 11기 4차 프로젝트 <br/>
> 팀 명: 미피 (美Pi, MePi)🐰 <br/>
> 기간: 2025.05.16 - 2025.06.11 <br/>

## 👤팀원 소개

<table align="center">
  <thead>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/9f719a4a-1b47-474e-b6b6-601e1f0b3750" width=200 alt="seongji"/><br />
      <a href='https://github.com/kimseoungji0801'>김성지</a><br />
    </td>
    <td align="center">
      <img src="https://github.com/yugyeongh.png" width=200 alt="yugyeong"/><br />
      <a href='https://github.com/yugyeongh'>현유경</a><br />
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/b3dddfe3-8be1-4bc3-be56-77d0c13f9442" width=200 alt="junghyun"/><br />
      <a href='https://github.com/Ohjunghh'>오정현</a><br />
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/cbf700b1-e4b0-4173-9af8-687f19cba69a" width="200" alt="misong"/><br />
      <a href='https://github.com/misong-hub'>백미송</a><br />
    </td>
  </thead>
</table>

<br/><br/>

# 🩷 프로젝트 개요

> 사용자의 피부 타입, 피부 고민, 보유 중인 화장품 등의 정보를 바탕으로, 궁합이 잘 맞는 기초 화장품이나 스킨케어 제품을 추천 서비스를 개발해 단순한 제품 매칭을 넘어, 화장품 성분 분석과 실제 사용자 리뷰 데이터를 기반으로 한 신뢰도 높은 정보를 제공하는 챗봇 

<br/>

## ☝🏻 프로젝트 필요성
최근 화장품을 선택할 때 제품의 성분을 중요시하는 소비자가 급격히 증가했습니다. 하지만 대다수의 소비자들은 화장품 성분의 구체적인 효능과 서로 다른 제품 간의 궁합에 대해서 명확하게 이해하지 못하고 있습니다. 성분에 대한 잘못된 정보나 부적절한 제품 조합은 피부 트러블 등의 문제를 유발할 수 있습니다. 이에 정확한 성분 정보 제공과 올바른 화장품 사용 가이드를 제공할 수 있는 도구의 필요성이 대두되었습니다.
<br/>

![image](https://github.com/user-attachments/assets/c9ef7647-1f9b-4564-a872-bca302756757)
![image](https://github.com/user-attachments/assets/2898b6ea-94df-4591-a18b-a7ba737a4fa5)


<br/>

## ⭐ 프로젝트 목표
1. 화장품 성분 정보를 사용자에게 명확하고 쉽게 제공하여 올바른 이해를 도움
2. 사용자가 보유한 화장품과의 궁합 분석을 통해 좋은 조합을 추천하고, 나쁜 조합에 대해서는 경고를 제공하여 피부 문제 예방에 도움
3. 맞춤형 성분 분석과 제품 추천을 통해 사용자가 더욱 건강하고 효율적인 피부 관리가 가능하도록 지원

<br/><br/>

# 📌 WBS

<table border="1">
  <thead>
    <tr>
      <th>단계</th>
      <th>주요 작업</th>
      <th>기간</th>
      <th>담당자</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>스킨케어 질문 데이터 수집</td>
      <td>25.05.24-25.05.25</td>
      <td>김성지, 백미송</td>
    </tr>
    <tr>
      <td>2</td>
      <td>데이터 전처리 및 정제</td>
      <td>25.05.26-25.05.27</td>
      <td>김성지,오정현</td>
    </tr>
    <tr>
      <td>3</td>
      <td>QLoRA 학습 데이터 생성</td>
      <td>25.05.28</td>
      <td>백미송, 현유경</td>
    </tr>
    <tr>
      <td>4</td>
      <td>FastAPI를 Django로 변환</td>
      <td>25.05.26-25.05.28</td>
      <td>김성지, 오정현</td>
    </tr>
    <tr>
      <td>5</td>
      <td>QLoRA 세팅 및 파인튜닝</td>
      <td>25.05.29-25.06.02</td>
      <td>백미송, 현유경</td>
    </tr>
    <tr>
      <td>6</td>
      <td>HTML/CSS를 활용한 UI 구현</td>
      <td>25.06.07-25.06.09</td>
      <td>김성지, 오정현</td>
    </tr>
<tr>
      <td>8</td>
      <td>AWS(EC2, RDS) 배포</td>
      <td>25.06.10</td>
      <td>김성지,현유경</td>
    </tr>
    <tr>
      <td>10</td>
      <td>통합 테스트 및 튜닝</td>
      <td>25.06.10</td>
      <td>ALL</td>
    </tr>
    <tr>
      <td>11</td>
      <td>발표 자료 / 코드 정리</td>
      <td>25.06.11</td>
      <td>ALL</td>
    </tr>
  </tbody>
</table>

<br/><br/>


# ✅ 기술 스택 & 사용한 모델

## 🔩 기술 스택

<table>
  <tbody>
    <tr>
      <td><strong>Language</strong></td>
      <td>
        <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
        <img src="https://img.shields.io/badge/CSS-663399?style=for-the-badge&logo=CSS3&logoColor=white">
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=black">
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
      </td>
    </tr>
    <tr>
      <td><strong>Framework</strong></td>
      <td>
        <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
      </td>
    </tr>
    <tr>
      <td><strong>AI/LLM & RAG</strong></td>
      <td>
        <img src="https://img.shields.io/badge/LangChain-000000?style=for-the-badge">
        <img src="https://img.shields.io/badge/ChromaDB-FFCC00?style=for-the-badge">
        <img src="https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black">
        <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
        <img src="https://img.shields.io/badge/RAG-4B8BBE?style=for-the-badge">
        <img src="https://img.shields.io/badge/QLoRA-8BC34A?style=for-the-badge">
      </td>
    </tr>
    <tr>
      <td><strong>Infra</strong></td>
      <td>
        <img src="https://img.shields.io/badge/RunPod-EE4C2C?style=for-the-badge">
        <img src="https://img.shields.io/badge/Amazon%20RDS-2D4999?style=for-the-badge&logo=Amazon%20RDS&logoColor=black"/>
        <img src="https://img.shields.io/badge/Amazon%20EC2-FFA500?style=for-the-badge&logo=Amazon%20EC2&logoColor=black"/>
    </tr>
  </tbody>
</table>

<br/><br/>

## 🤖 사용한 모델
<table>
  <thead>
    <tr>
      <th>역할</th>
      <th>모델</th>
      <th>플랫폼</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>문서 임베딩</td>
      <td>snunlp/KR-SBERT-V40K-klueNLI-augSTS</td>
      <td>
        <img src="https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black">
      </td>
    </tr>
    <tr>
      <td>QA 데이터 생성 (RAG 기반)</td>
      <td>GPT-4o-mini</td>
      <td>
        <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
      </td>
    </tr>
    <tr>
      <td>파인튜닝 사전 학습 모델</td>
      <td>EleutherAI/polyglot-ko-1.3b</td>
      <td>
        <img src="https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black">
      </td>
    </tr>
    <tr>
      <td>사용자 정의 모델</td>
      <td><a href="https://huggingface.co/piboo/PiBoo" target="_blank">piboo/PiBoo</a></td>
      <td>
        <img src="https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black">
      </td>
    </tr>
  </tbody>
</table>

<br/><br/>

# 🪼 시스템 아키텍처
<img src="https://github.com/user-attachments/assets/55d5cc30-65be-4341-8fc1-b23c3938d793" width="750">

<br/>

## ✅ 시스템 아키텍처 간략 설명

### 1. EC2 (AWS)
- Django 서버가 호스팅된 인프라 환경
- 프론트엔드, 백엔드, RAG 흐름을 연결하는 중심 역할 수행

### 2. Django (Docker)
- API 서버 역할
- 사용자 질문을 받아 RAG 시스템에 전달하고, 결과를 반환

#### 🖥️ Web Frontend (Django Template)
- 사용자 인터페이스는 Django 템플릿으로 구현
- HTML 파일은 `templates` 폴더에 위치
- CSS, 이미지(jpg) 등 정적 파일은 `static` 폴더에서 관리
- 사용자가 질문 입력 및 답변 확인 가능

#### 📦 RAG 시스템 구성
- **문서 검색 소스**: `oliveyoung_final.csv`, `preprocessed_ingredients.csv`
- **임베딩 모델**: `snunlp/KR-SBERT-V40K-klueNLI-augSTS`
- **구성 요소**: LangChain + Chroma
- 질문에 적합한 문서를 추출하고, RDS에 저장된 이전 대화 내역을 반영하여 프롬프트 구성

### 3. RunPod (piboo/PiBoo 모델)
- HuggingFace 기반 사용자 정의 LLM 사용
- 문서 + 질문을 기반으로 답변 생성
- GPU 환경에서 고속 추론 처리

### 4. OpenAI (GPT-4o-mini)
- RunPod 대신 활용 가능한 백업 또는 보조 LLM
- 높은 품질의 응답을 생성하는 데 사용

### 5. Amazon RDS (MySQL)
- 질문, 답변, 사용자 데이터, 대화 이력 저장
- Django 백엔드와 연동하여 데이터 관리 수행

<br/><br/>

# 📄 요구사항 명세서
![image](https://github.com/user-attachments/assets/6a01ab54-86de-4dc1-be5c-5fba4e2b042c)

<br/><br/>
<h2>🖌️ 화면 설계서(Figma)</h2>

## 메인

<img src="https://github.com/user-attachments/assets/f6aed9af-b2cf-4628-ba08-0a8f1ffbacf6" width="750">


## 로그인

<img src="https://github.com/user-attachments/assets/d2498d9f-7fbc-4c75-a2b3-115dc8f00c88" width="750">


## 회원가입


## 챗봇



<br/><br/>



# 📜 수집한 데이터 및 전처리 요약
> 1. `question.csv`: 화장품 관련 카페의 스킨케어 Q&A칸에서 제목, 본문 2가지의 항목을 크롤링
> 2. `preprocesssed_oliveyoung.csv`: final_oliveyoung.csv의 reveiws열을 요약한 새로운 열을 추가
<br/>


## 스킨케어 질문 크롤링

  <img width="834" alt="cafe_skincare" src="https://github.com/user-attachments/assets/5adcb03c-bce8-4fb8-91e3-14689d893c14" />

<br/>

## ☝🏻 전처리 과정

### 🫒 skincare_qa.csv </br> 
### 원본 데이터  </br> 
![image](https://github.com/user-attachments/assets/ba3df277-8d38-484a-9293-844dc4ae7722)
 </br>

### Title , body 전처리  
![image](https://github.com/user-attachments/assets/725e2a43-dabe-4621-99b8-bd3fe45727d1)
 
 </br> 
 
 ---
 
### 🍭preprocessed_oliveyoung.csv </br> 
### 원본 데이터  </br> 
![Image](https://github.com/user-attachments/assets/daa48044-27f8-450f-8948-88ee3acf23cf)

 </br>

### reviews 전처리 ( GPT-4o-mini를 사용하여 요약)
![Image](https://github.com/user-attachments/assets/22c36118-7240-45c4-939c-5a2ad7f0aec5)

</br>

- `review_summaries`열 생성
  - 리뷰에서 반복적으로 언급된 특징을 한 문장씩 bullet point로 2~5개 추출

    
- `keywords`열 생성
  - 리뷰에서 자주 등장하는 핵심 키워드를 최대 5개까지 추출
    
    
- `document`열 생성
  - 전체 리뷰의 분위기, 주요 의견, 실제 사용 상황, 다양한 피부 타입 경험 등을 3~5문장 요약
    
</br>


--- 

# ☁️ 테스트 계획 및 결과 보고서

<table border="1" cellspacing="0" cellpadding="8">
  <thead>
    <tr>
      <th>Test ID</th>
      <th>목적</th>
      <th>입력 예시</th>
      <th>기대 결과</th>
      <th>실제 결과</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CASE01</td>
      <td>메인페이지에서 회원가입 버튼 클릭시 정상적으로 이동하는지 확인</td>
      <td>회원가입 버튼 클릭</td>
      <td>회원가입 페이지로 이동</td>
      <td><img src="https://github.com/user-attachments/assets/47245cc9-6224-44c6-abb4-f5daab58aeb0"/></td>
    </tr>
    <tr>
      <td>CASE02</td>
      <td>회원가입 시 중복 검사를 통과하고 모든 조건 충족 시 로그인 창으로 이동하는지 확인</td>
      <td>사용 가능한 아이디/닉네임 + 일치하는 비밀번호 입력 후 회원가입</td>
      <td>회원가입 완료 후 로그인 창으로 이동</td>
      <td><img src="https://github.com/user-attachments/assets/49943985-ec84-4d81-bb26-b3d31a18fa6e"/></td>
    </tr>
    <tr>
      <td>CASE03</td>
      <td>로그인 성공 여부에 따라 페이지가 정상적으로 이동하는지 확인</td>
      <td>정상적인 아이디/비밀번호 입력 후 로그인</td>
      <td>로그인 성공 시 챗봇 페이지로 이동</td>
      <td><img src="https://github.com/user-attachments/assets/7896afd1-8502-40e8-a0cd-6adc14651583"></td>
    </tr>
    <tr>
      <td>CASE04</td>
      <td>챗봇이 질문 의도에 따라 RAG 문서를 활용한 적절한 답변을 반환하는지 확인</td>
      <td>예시 질문: "나는 지성피부야 끈적거리지 않는 앰플을 추천 받고 싶어"</td>
      <td>질문 의도에 맞는 답변 + 관련 문서 기반 정보 제공</td>
      <td><img src="https://github.com/user-attachments/assets/d5b24ec7-0890-422b-810b-2fb0d0764593"></td>
    </tr>
    <tr>
      <td>CASE05</td>
      <td>챗봇이 이전 대화를 활용하여 답변을 반환하는지 확인</td>
      <td>예시 질문: "내 피부타입은 지성이야", "내 피부타입은?"</td>
      <td>이전 대화를 활용하여 답변 제공</td>
      <td><img src="https://github.com/user-attachments/assets/297e6751-bd27-4396-b960-7877fa991519"></td>
    </tr>
    <tr>
      <td>CASE06</td>
      <td>챗봇이 이전 대화를 RDS에서 정상적으로 불러오는지 확인</td>
      <td>예시 질문: "이전 질문을 말해줘"</td>
      <td>이전 질문 내역을 제공</td>
      <td><img src="https://github.com/user-attachments/assets/8e87c4c8-19af-4448-bc40-66538e52b973"></td>
    </tr>
    <tr>
      <td>CASE07</td>
      <td>메시지 입력칸 비우기 버튼이 채팅창 화면이 초기화 되는지 확인</td>
      <td>입력칸 비우기 버튼 클릭</td>
      <td>입력란의 텍스트가 아닌, 채팅창 화면이 초기화</td>
      <td><img src="https://github.com/user-attachments/assets/5be6a89c-5ca3-4934-a75a-a69fa58d258b"></td>
    </tr
    <tr>
      <td>CASE08</td>
      <td>마이페이지에서 최근 대화 내용을 정확히 불러오는지 확인</td>
      <td>마이페이지 접속</td>
      <td>시간 순으로 최근 대화 내용 출력</td>
      <td><img src="https://github.com/user-attachments/assets/9ea48593-18e6-4e30-8b55-96d121cacad7"></td>
</td>
    </tr>
  </tbody>
</table>


<br/><br/>

# 수행결과(테스트/시연 페이지)
## 🎨 Frontend  
Figma로 설계된 디자인 시안을 바탕으로,  HTML,CSS 사용자 인터페이스를 구현

### 🖌️ 화면 초안(Figma) & 구현 결과 비교

| 메인화면 초안 | 현재 구현 결과 |
|-----------------|----------------|
| ![메인화면](https://github.com/user-attachments/assets/2e5fc06e-dd30-45cb-898f-3b7e4a32e7de) | ![](https://github.com/user-attachments/assets/f50c330b-b149-4292-a4c7-43cec7108e08) |
| **로그인 화면 설계서** | **로그인 화면 구현** |
| ![로그인](https://github.com/user-attachments/assets/d5696fc1-0ee5-42f3-a173-4c4ce409361d) | <img src="https://github.com/user-attachments/assets/49943985-ec84-4d81-bb26-b3d31a18fa6e"/> |
| **회원가입 화면 설계서** | **회원가입 화면 구현** |
 <img src="https://github.com/user-attachments/assets/7306f66c-fd80-4365-9379-4cc9a9faf1be" width="300"> | <img src="https://github.com/user-attachments/assets/47245cc9-6224-44c6-abb4-f5daab58aeb0"/>
| **챗봇 화면 설계서** | **챗봇 화면 구현** |
   <img src="https://github.com/user-attachments/assets/55f10dc2-ee47-4550-b752-034fb02a19a4" width="300"><br>|<img src="https://github.com/user-attachments/assets/7896afd1-8502-40e8-a0cd-6adc14651583" width=990/>
---

## 📱 새로 추가된 화면
  <img src="https://github.com/user-attachments/assets/4afd209a-9685-4548-9549-e0760000c946" width="1000"/>


---

## 🤹 시연
#### 회원가입 & 로그인
![Image](https://github.com/user-attachments/assets/22bbeb97-a785-452f-9a3b-f1065bcfe560)

</br> 

#### 챗봇
![Image](https://github.com/user-attachments/assets/cb3252c7-ac75-418f-a5d8-d40c8905a987)

</br> 

#### 마이페이지 & 대화 비우기
![Image](https://github.com/user-attachments/assets/f0e008e1-7d36-44ab-97f4-c1dd5ec94e7e)

</br> 

#### 메인화면 돌아가기 & 로그아웃
![Image](https://github.com/user-attachments/assets/f5469011-b6a9-45bb-b3ed-86fcc0d74e9d)



</br> </br> 


## 🗂️ DB
**Django ORM을 활용하여 AWS RDS와 연동하고, 아래 두 모델 기반으로 데이터를 효율적으로 저장**

### 1. 📄 User

`사용자 인증 및 프로필 정보를 관리하는 모델. Django의 AbstractUser를 확장하여 커스터마이징`
</br>


| 필드명     | 자료형              | 설명                                |
|------------|---------------------|-------------------------------------|
| username   | `CharField`         | 사용자 ID (기본 필드)               |
| password   | `CharField`         | 비밀번호 (기본 필드)                |
| nickname   | `CharField(50)`     | 사용자 닉네임 (고유, 필수 입력)     |
| age        | `PositiveIntegerField` | 나이 (선택 입력)                |
| gender     | `IntegerField`      | 성별 (0: 남자, 1: 여자, 선택 입력) |
|  -         | -                  | `AbstractUser`의 기본 필드 포함     |


### 2. 📄 ChatLog

`사용자의 질문과 챗봇의 응답을 저장하는 기록 테이블`

</br>

| 필드명     | 자료형             | 설명                             |
|------------|--------------------|----------------------------------|
| nickname   | `CharField(100)`   | 질문자의 닉네임                  |
| question   | `TextField`        | 사용자의 질문 내용                |
| answer     | `TextField`        | 챗봇의 응답 내용                  |
| created_at | `DateTimeField`    | 질문 생성 시각 (자동 저장)       |

</br></br>

---

## 🛠️ Backend
#### 📡 API 명세서

|  기능  | 기능 설명                    | HTTP | API Path                             |
|--------|------------------------------|------|--------------------------------------|
|질문 수신| 사용자 질문 받음             | POST | `/api/chatbot/ask`                  |
|질문 전송| Django → RunPod로 질문 전송  | POST | `/api/runpod/question`           |
|답변 수신| RunPod → Django로 답변 전송  | POST | `/api/runpod/answer`  |
|답변 전송| Django → Front로 답변 전송  | POST | `/api/runpod/answer`  |

</br> 

#### 🎀 프로젝트 구조
```
backend/
│  .env                # 환경변수 설정 파일
│  .gitignore          # Git에서 무시할 파일 목록
│  docker-compose.yaml # Docker Compose 설정 파일
│  Dockerfile          # Docker 이미지 빌드 설정
│  gunicorn.conf.py    # Gunicorn 웹서버 설정
│  manage.py           # Django 프로젝트 관리 명령어
│  requirements.txt    # 파이썬 패키지 의존성 목록
│
├─backend
│  ├─urls.py          # 앱(chatbot, users 등) URL 라우팅 및 메인 페이지 구성
│  └─views.py         # 메인 페이지 렌더링 및 기본 뷰 로직
│
├─chatbot
│  ├─chain.py         # LangChain 관련 체인(프롬프트/답변 흐름 관리)
│  ├─models.py        # ChatLog 모델(챗봇 대화 내역 저장)
│  ├─qlora.py         # LangChain과 파인튜닝 모델(QLoRA) 연결용 클래스 정의
│  ├─urls.py          # 챗봇 앱 URL 라우팅
│  ├─views.py         # 챗봇 앱 뷰(API 엔드포인트 및 로직)
│  └─prompt
│    ├─gpt_templates.py   # GPT 프롬프트 템플릿
│    └─qlora_templates.py # QLoRA 프롬프트 템플릿
│
├─history
│  └─utils.py         # 채팅 내역 관련 함수
│
├─retriever
│  └─utils.py         # RAG 관련 함수
│
├─static
│  ├─images
│  │  └─intro.png    # 인트로 페이지 이미지
│  └─style
│    ├─chatbot.css    # 챗봇 페이지 스타일
│    ├─intro1.css     # 인트로 페이지 스타일 
│    ├─login.css      # 로그인 페이지 스타일
│    ├─mypage.css     # 마이페이지 스타일
│    └─signup.css     # 회원가입 페이지 스타일
│
├─templates
│  ├─chatbot1.html    # 챗봇 페이지 템플릿
│  ├─index.html       # 메인 페이지 템플릿
│  ├─login.html       # 로그인 페이지 템플릿
│  ├─mypage.html      # 마이페이지 템플릿
│  └─signup.html      # 회원가입 페이지 템플릿
│
├─users
│  ├─admin.py         # 관리자 페이지 설정
│  ├─forms.py         # 로그인/회원가입 폼
│  ├─models.py        # 사용자(User) 정보 저장 모델
│  ├─tests.py         # 테스트 코드
│  ├─urls.py          # 사용자 앱 URL 라우팅
│  └─views.py         # 사용자 앱 뷰(회원가입, 로그인 등)
│
└─vectordb
  ├─cosmetic_chromadb      # 화장품 벡터 데이터베이스
  └─ingredient_chromadb    # 성분 벡터 데이터베이스
```

---

# 🚨 개선 사항
<img src="https://github.com/user-attachments/assets/018e5918-d92b-4038-8519-d84c576f7ae7" width=750/>

> ※ 3차 때 개선 사항

---
## 주요 개선 사항 요약
## 1. 모델 성능 개선

기존 QLoRA 파인튜닝 모델은 약 100개의 QA 데이터로 학습되어 **일반화 성능에 한계**가 있었습니다.  
이를 개선하기 위해 `EleutherAI/polyglot-ko-1.3b` 모델로 교체하고,  
**약 3,000개의 QA 쌍**을 새롭게 구축하여 재학습을 진행했습니다.

- ✅ **개선**:  
  모델 교체와 다량의 QA 데이터로 재학습 수행

- 🔧 **계획**:  
  Loss가 일부 감소했으나 응답 정확도와 일관성이 부족하여,  
  더 많은 **고품질 QA 데이터 확보** 및 **추가 학습** 진행 예정
---

### 2. 웹 버전 UI 개선

- 🔍 **기존 문제**:  
  기존 UI는 모바일에만 최적화되어 있어 다양한 환경에서 사용이 어려움

- ✅ **개선** :  
  Django + HTML 기반의 웹 UI로 전환하여  
  데스크탑 환경에서도 접근 가능하도록 개선

- 🔧 **계획**:  
  사용자 피드백 기반으로 반응형 디자인 보완 및 기능 고도화 예정

---

## 3. 문서 임베딩 처리 오류 개선

리뷰 데이터가 길어 토큰 수가 많은 경우,  
임베딩 과정에서 오류가 발생하거나 VectorDB에 저장되지 않는 문제가 있었습니다.

- 🔍 **기존 문제**: 긴 리뷰 데이터 → 처리 오류 발생
- ✅ **개선**:  
  - 긴 리뷰 100개를 분석하여  
    **핵심 리뷰 약 5개**, **중요 키워드 5개**, **전체 요약 1개**를 생성  
  - 토큰 수를 줄여 **오류 최소화** 및 **요약 기반 응답 품질 향상** 시도 

---

# ✅ 한 줄 회고
| 팀원  | 한 줄 회고                 |
|-------|----------------------------|
| 미송  | 3차 프로젝트에서는 파인튜닝이 기대만큼 잘 이루어지지 않아 아쉬움이 컸습니다. 이를 보완하고자 4차 프로젝트에서는 데이터를 더 많이 수집해 QA 쌍을 늘리고, 모델 구조도 변경하여 다시 파인튜닝을 시도했습니다. 그 결과, 이전보다 더 나은 응답을 생성할 수 있었지만, 여전히 아쉬움이 남았습니다. 앞으로는 더 풍부하고 다양한 데이터를 활용해 더욱 정교한 모델을 완성해보고 싶습니다. 또한 이번 프로젝트를 통해 AWS에 대한 이해를 넓히게 되었고, 최종 프로젝트에서는 모델 개발뿐만 아니라 직접 AWS를 활용해 배포까지 완성도 높게 마무리하는 것을 목표로 삼게 되었습니다. 아직 부족한 점은 많지만, 이번 프로젝트를 진행하면서 스스로가 조금씩 성장하고 있다는 것을 느꼈고, 함께 고생한 팀원들과 저 자신에게도 박수를 보내고 싶습니다.|
| 정현  | FastAPI로 구현된 백엔드를 Django로 재구성하며 이해도가 많이 높아졌습니다.프론트엔드 작업도 생각보다 화면을 더 보기 좋게 꾸미는 과정이 재미있었습니다!3차 때 못 해봤던 QLoRA 파인튜닝도 이번에는 시도해볼 수 있어서 좋았습니다.도커와 AWS는 아직 어렵지만, 최종 프로젝트에서는 도전해보고 싶습니다.3차에서 4차까지 이어서 프로젝트를 진행하며, 긴 기간 덕분에 꾸준히 성장하는 것을 느끼고 다양한 경험을 쌓을 수 있어 의미 있는 시간이었습니다. 모두들 수고하셨습니다! |
| 유경  | - |
| 성지  | - |
