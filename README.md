## 설치방법

0. requirments.txt 설치
1. MYSQL 설치
2. MYSQL 사용자/비밀번호 settings에 입력
3. 데이터베이스 'memos' 생성
4. URL localhost:8000/create-db-table 접속 (테이블 생성)

<br>

## 실행방법

- 서버실행 : uvicorn main:app --reload

<br>

## API 문서

- Swagger 확인 : localhost:8000/docs

<br>

## 기술스택

- python 3.10
- FastAPI, SQLAlchemy
- MYSQL
