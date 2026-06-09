# BSS (Better Smart Spending) - 스마트 소비 관리 프로그램

## 📋 프로젝트 개요
일상적으로 사용하는 물건의 소비 주기를 직접 입력하면, 해당 주기에 맞춰 알림을 제공하는 스마트 소비 관리 프로그램입니다. 사용자의 소비 패턴을 분석하여 MBTI 형식의 소비 유형으로 분류함으로써, 사용자가 자신의 소비 습관을 직관적으로 파악할 수 있도록 합니다.

## 🎯 핵심 목표
- **소비 주기 관리**: 사용자가 물품별 교체/재구매 주기를 등록하고, 시기에 맞는 알림을 수신
- **소비 습관 가시화**: 소비 데이터를 축적·분석하여 개인화된 소비 유형 리포트 제공
- **행동 변화 유도**: 소비 유형 분류(소비 MBTI) 기능을 통해 불필요한 충동 구매 감소
- **사용자 경험 향상**: 직관적인 UI/UX를 통해 모든 연령대가 쉽게 사용 가능

## 📁 프로젝트 구조
```
BSS/
├── backend/                    # 백엔드 (Flask)
│   ├── app.py                 # 메인 애플리케이션
│   ├── models.py              # 데이터베이스 모델
│   ├── routes.py              # API 라우트
│   ├── services/
│   │   ├── product_service.py # 물품 관리 서비스
│   │   ├── consumption_service.py # 소비 추적 서비스
│   │   └── mbti_service.py    # 소비 MBTI 분석 서비스
│   └── requirements.txt        # 의존성
├── frontend/                   # 프론트엔드 (HTML/CSS/JS)
│   ├── index.html             # 홈 페이지
│   ├── dashboard.html         # 대시보드
│   ├── analysis.html          # 분석 페이지
│   ├── css/
│   │   └── style.css          # 스타일시트
│   └── js/
│       ├── app.js             # 메인 JavaScript
│       └── api.js             # API 호출 함수
├── database/
│   └── init_db.py             # 데이터베이스 초기화
└── README.md
```

## 🚀 시작하기

### 1. 환경 설정
```bash
# 저장소 클론
git clone https://github.com/digitaltutor26/BSS.git
cd BSS

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Mac/Linux
# 또는
venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r backend/requirements.txt
```

### 2. 데이터베이스 초기화
```bash
python database/init_db.py
```

### 3. 백엔드 실행
```bash
cd backend
python app.py
```

### 4. 프론트엔드 접속
- 브라우저에서 `http://localhost:5000`으로 접속

## 💡 주요 기능

### 1. 소비 주기 관리
- 물품 등록 (카테고리, 구매 가격, 사용 주기)
- 구매 이력 기록
- 예정된 구매 알림

### 2. 소비 패턴 분석
- 월별/카테고리별 소비액 통계
- 소비 추이 시각화
- 개인화된 소비 보고서

### 3. 소비 MBTI 분류
- 4가지 소비 성향 차원 분석
- 16가지 소비 유형 분류
- 맞춤형 소비 개선 제안

## 🛠 기술 스택
- **백엔드**: Python, Flask
- **데이터베이스**: SQLite
- **프론트엔드**: HTML5, CSS3, JavaScript
- **차트**: Chart.js

## 📝 라이선스
MIT License

## 👨‍💻 개발자
digitaltutor26
