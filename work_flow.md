# (예상) 작업순서

## 1. install dependancy

- python 3.10
- bcrypt
- JWT
  <br>
  <br>

## 2. directory create

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
  - secrets
    - DB_URL
    - JWT_ALGO, JWT_SECRET_KEY
- README.md
- .gitignore
- requirements.txt
  <br>
  <br>

## 3. create main.py

1. API

<br>
<br>

## 3.5 create DB connection

## 4. user

1. model
2. schema
3. API
   - sign up
   - sign in
   - check JWT
     <br>
     <br>

## 5. memo

1. model
2. schema
3. API
   - GET list
   - GET one
   - CREATE memo
   - UPDATE memo
   - DELETE memo

## 6. reply

1. model
2. schema
3. API
   - CREATE reply
   - UPDATE reply
   - GET reply (with GET one in memo)
