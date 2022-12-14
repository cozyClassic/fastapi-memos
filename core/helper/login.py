from datetime import datetime

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from core.config.secrets import ALGORITHM, SECRET_KEY
from .constants import DATE_TIME_FORM



async def get_current_user(token:str = Depends("")):
    if not token:
        return {"success":False, "message": "token not found"}

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
        raise credentials_exception

    return {"success":True, "user_id": payload["user_id"]}
