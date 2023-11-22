from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from fastapi import Depends, HTTPException, status
from db.database import get_db
from sqlalchemy.orm.session import Session
from db import db_user
from db.db_user import *

 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
 
SECRET_KEY = '3aab7bf1db3d3d855e54aad5594b0016ed03344085bb90efadaa6bfc918055c8'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
 
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()

  if expires_delta:
    expire = datetime.utcnow() + expires_delta

  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
    
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

  return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
  # standard way to raise an exception of authentication user 
  credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
  )

  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")

    if username is None:
      raise credentials_exception

  except JWTError:
    raise credentials_exception
  
  user = db_user.CrudUser.get_user_by_username(username,db)

  if user is None:
    raise credentials_exception
  
  return user