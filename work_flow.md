# (예상) 작업순서

## 1. install dependancy (DONE)

- python 3.10
- bcrypt
- JWT
  <br>
  <br>

## 2. directory create (DONE)

- core
  - users
    - model
    - schema
    - router
  - memos
    - model
    - schema
    - router
  - reply
    - model
    - schema
    - router
  - helper
    - jwt checker
    - create_at, delete_at(model, schema)
  - database
    - engine, Session, get_db
  - config
    - secrets : DB_URL, JWT_ALGO, JWT_SECRET_KEY
- README.md
- .gitignore
- requirements.txt
  <br>
  <br>

## 3. create main.py (Done)

1. API

<br>
<br>

## 3.5 create DB connection (확인 안됨)

## 4. user

1. model (done)
2. schema (done)
3. API

   - sign up (Done)
   - sign in (Done)
   - check JWT (Done)
   - validator (Done)
     <br>
     <br>

## 5. memo

1. model (Done)
2. schema (Done)
3. API
   - GET list (Done)
   - GET one (Done)
   - CREATE memo (Done)
   - UPDATE memo
   - DELETE memo

## 6. reply

1. model
2. schema
3. API
   - CREATE reply
   - UPDATE reply
   - GET reply (with GET one in memo)
