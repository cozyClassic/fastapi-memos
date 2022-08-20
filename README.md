## 설치방법

0. 가상환경
   - python 3.10.4 설치 및 활성화
   - pip install -r requirements.txt
1. MYSQL 설치 및 실행
2. 데이터베이스 'memos' 생성 (한글 사용하도록 주의)
3. 첨부한 secrets.py에 DB 접속 계정,비밀번호 수정
   - secrets.py 경로 : core/config/secrets.py

<br>

## 실행방법

- 서버실행 : uvicorn main:app --reload
- 메모 데이터를 생성하려면 sign-up을 먼저 해야 합니다.
- sample_jwt는 user_id=1 이 담겨있습니다.

<br>

## API 문서

- Swagger 확인 : localhost:8000/docs

<br>

## 기술스택

- python 3.10.4
- FastAPI, SQLAlchemy
- MYSQL
- bcrypt, JWT
