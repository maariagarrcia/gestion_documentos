from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from db.database import get_db
from sqlalchemy.orm.session import Session
from typing import Optional
from db import models
from db.hash import Hash
from auth import oauth2
from fastapi.responses import JSONResponse



router = APIRouter(
    tags=["authentication"]
)

@router.post("/token")
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.DbUser).filter(
        models.DbUser.username == request.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    if not Hash.verify(user.hashed_password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

    access_token = oauth2.create_access_token(data={"sub": user.username})

    response= JSONResponse(content={"access_token": access_token, "token_type": "bearer", "user_id": user.id, "username": user.username})
    response.set_cookie(key="access_token", value=f"{access_token}")
    response.set_cookie(key="token_type", value="bearer")
    response.set_cookie(key="user_id", value=f"{user.id}")
    response.set_cookie(key="username", value=f"{user.username}")

    return response

