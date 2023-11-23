from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File
from sqlalchemy.orm import Session


from db.database import get_db
from db import db_file
from db.db_file import CrudFile
from db.models import DbFile

from schemas import FileBaseModel, FileDisplayModel,UserAuth

from typing import List

import random
import string
import shutil

from auth.oauth2 import get_current_user

import os

router = APIRouter(
    prefix="/file",
    tags=["file"]
)


tipo_url = ["absolut", "relative"]


@router.post("/create_file", response_model=FileDisplayModel)
async def create_file(request: FileBaseModel, db: Session = Depends(get_db), current_user:UserAuth = Depends(get_current_user)):
    if not request.tipo_url in tipo_url:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter tipo_url is not valid only absolut or relative")
    return db_file.CrudFile.create_file(db, request)


@router.get("/get_all", response_model=List[FileDisplayModel])
async def get_all(db: Session = Depends(get_db),current_user:UserAuth = Depends(get_current_user)):
    return db_file.CrudFile.get_all(db)



ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".avi", ".mkv", ".pdf", ".txt", ".doc", ".docx", ".odt", ".svg", ".webp", ".jfif", ".webm", ".mov", ".wmv", ".flv", ".3gp"}

def get_user_folder(user_id: int):
    # Cambia esta función según cómo estés manejando las carpetas de los usuarios
    # Puedes usar el ID del usuario para crear carpetas únicas para cada usuario.
    user_folder = f"./files/users/{user_id}/"
    os.makedirs(user_folder, exist_ok=True)
    return user_folder

@router.post("/uploadfile/")
async def upload_file(upload_file: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user), folder_name: str = ""):
    file_ext = os.path.splitext(upload_file.filename)[1]

    if file_ext.lower() not in ALLOWED_EXTENSIONS:
        return {"error": "Formato de archivo no permitido"}

    user_folder = get_user_folder(current_user.id)

    if folder_name:
        user_folder = os.path.join(user_folder, folder_name)
        os.makedirs(user_folder, exist_ok=True)

    filename = upload_file.filename
    path = os.path.join(user_folder, filename)

    with open(path, 'wb') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return {"filename": path}


@router.delete("/delete_file/{id}")
async def delete_file(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    file = db_file.CrudFile.delete_file(id, db, current_user.id)
    return {"message": "ok"}
