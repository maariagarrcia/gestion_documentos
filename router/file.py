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


@router.get("/get_all", response_model=List[FileDisplayModel],)
async def get_all(db: Session = Depends(get_db),current_user:UserAuth = Depends(get_current_user)):
    return db_file.CrudFile.get_all(db)


ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".avi", ".mkv", ".pdf", ".txt"}

@router.post("/uploadfile/")
async def upload_file(upload_file: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    file_ext = os.path.splitext(upload_file.filename)[1]

    if file_ext.lower() not in ALLOWED_EXTENSIONS:
        return {"error": "Formato de archivo no permitido"}

    # Genera un nombre único para el archivo
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(upload_file.filename.rsplit('.', 1))

    if file_ext.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".jfif"}:
        path = f'./files/images/{filename}'
    elif file_ext.lower() in {".mp4", ".avi", ".mkv",".webm", ".mov",".wmv",".flv",".3gp"}:
        path = f'./files/videos/{filename}'
    elif file_ext.lower() == ".pdf":
        path = f'./files/docs/pdf/{filename}'
    elif file_ext.lower() == {".txt", ".doc", ".docx", ".odt"}:
        path = f'./files/docs/text/{filename}'
     
    else:
        return {"error": "Tipo de archivo no reconocido"}
    
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {"filename": path}



@router.delete("/delete_file/{id}")
async def delete_file(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    file = db_file.CrudFile.delete_file(id, db, current_user.id)
    return {"message": "ok"}
