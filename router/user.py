from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from schemas import UserBaseModel, UserDisplayModel

from db.database import get_db
from db import db_user
from db.db_user import CrudUser

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from auth import authentication
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/user',
    tags=['Users']
)
router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@router.post('/create', response_model=UserDisplayModel)
async def create_user(request: UserBaseModel, db: Session = Depends(get_db)):
    return db_user.CrudUser.create_user(db, request)

@router.get('/get_all', response_model=List[UserDisplayModel])
async def get_all_users(db: Session = Depends(get_db)):
    return db_user.CrudUser.get_all(db)

@router.get('/login', response_model=UserDisplayModel)
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return db_user.CrudUser.get_user_by_username(username, db)

@router.put('/{id}', response_model=UserDisplayModel)
async def update_user(id: int, request: UserBaseModel, db: Session = Depends(get_db)):
    return db_user.CrudUser.update_user(id, request, db)

@router.delete('/{id}/delete')
async def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.CrudUser.delete_user(id, db)

