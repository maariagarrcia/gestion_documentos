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

# create user
@router.post('/',response_model=UserDisplayModel)
def create_users(request:UserBaseModel, db:Session = Depends(get_db)):
    return db_user.CrudUser.create_user(db, request)

# read all  users: el query simplemente es un select * from user para oobtenr los datos del usuario
@router.get('/', response_model=List[UserDisplayModel])
def get_all_users(db:Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    return db_user.CrudUser.get_all_users(db)

# read 1 user
@router.get('/{id}', response_model=UserDisplayModel)
def get_user_by_id(id:int, db:Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    return db_user.CrudUser.get_user_by_id(db, id)


# update user
@router.post('/{id}/update', response_model=UserDisplayModel)
def update_user(id:int, request:UserBaseModel, db:Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    return db_user.CrudUser.update_user(db, id, request)


# delete user
@router.get('/{id}/delete')
def delete_user(id:int, db:Session = Depends(get_db),current_user:UserBaseModel = Depends(get_current_user)):
    return db_user.CrudUser.delete_user(db, id)
