from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from sqlalchemy.orm import Session
from schemas import UserBaseModel, UserDisplayModel,CarpetaDisplayModel,CarpetaBaseModel

from db.database import get_db
from db import db_carpeta
from db.db_carpeta import CrudCarpeta

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from auth import authentication
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/carpeta',
    tags=['Carpeta']
)
router.mount("/static/css/", StaticFiles(directory="static/css"), name="static")
router.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@router.post("/create_carpeta", response_model=CarpetaDisplayModel)
async def create_carpeta(request: CarpetaBaseModel, db: Session = Depends(get_db)):
    return db_carpeta.CrudCarpeta.create_carpeta(db=db, request=request)

@router.get("/get_carpeta/{id}")
async def get_carpeta(id: int, db: Session = Depends(get_db)):
    return db_carpeta.CrudCarpeta.get_carpeta(db, id)

@router.get("/get_all_carpeta")
async def get_all_carpeta(db: Session = Depends(get_db)):
    return db_carpeta.CrudCarpeta.get_all_carpeta(db)

@router.put("/update_carpeta/{id}", response_model=CarpetaDisplayModel)
async def update_carpeta(id: int, request: CarpetaDisplayModel, db: Session = Depends(get_db)):
    return db_carpeta.CrudCarpeta.update_carpeta(db=db, id=id, request=request)

@router.delete("/delete_carpeta/{id}")
async def delete_carpeta(id: int, db: Session = Depends(get_db)):
    return db_carpeta.CrudCarpeta.delete_carpeta(db=db, id=id)


