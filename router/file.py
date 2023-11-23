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



# Definir extensiones permitidas
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".avi", ".mkv", ".pdf", ".txt", ".docx", ".doc", ".odt", ".rtf", ".tex", ".wks", ".wps", ".wpd", ".mov", ".wmv", ".flv", ".webm", ".bmp", ".ico", ".webp"}

# Ruta para manejar la carga de archivos
@router.post("/uploadfile")
async def upload_file(upload_file: UploadFile = File(...)):
    file_ext = os.path.splitext(upload_file.filename)[1].lower()  # Convertir la extensión a minúsculas

    if file_ext not in ALLOWED_EXTENSIONS:
        return {"error": "Formato de archivo no permitido"}

    # Genera un nombre único para el archivo
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new_filename = f"{rand_str}{file_ext}"

    # Construye la ruta completa del archivo según su tipo
    if file_ext in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".ico", ".webp"}:
        file_path = f"files/images/{new_filename}"

    elif file_ext in {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"}:
        file_path = f"files/videos/{new_filename}"

    elif file_ext == ".pdf":
        file_path = f"files/docs/pdf/{new_filename}"
        
    elif file_ext in {".txt", ".docx", ".doc", ".odt", ".rtf", ".tex", ".wks", ".wps", ".wpd"}:
        file_path = f"files/docs/text/{new_filename}"
    else:
        return {"error": "Tipo de archivo no reconocido"}

    # Guarda el archivo en la ruta deseada
    with open(file_path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)

    return {"filename": file_path}


@router.delete("/delete_file/{id}")
async def delete_file(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    file = db_file.CrudFile.delete_file(id, db, current_user.id)
    return {"message": "ok"}
