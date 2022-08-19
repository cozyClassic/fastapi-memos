from datetime import datetime

from fastapi import Depends, HTTPException, status
from core.config.secrets import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError

from .constatns import DATE_TIME_FORM

async def get_current_user(token:str = Depends("")):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    
    except JWTError:
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"})
        raise credentials_exception

    token_expire = datetime.strptime(payload["expire_at"], DATE_TIME_FORM)
    if token_expire < datetime.now():
        return {"success":False, "message": "token expired"}

    return {"success":True, "user_id": payload["user_id"]}