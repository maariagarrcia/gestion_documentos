from fastapi import APIRouter, HTTPException, Depends, status, UploadFile, File
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_file
from db.db_file import CrudFile
from db.models import DbFile
from schemas import FileBaseModel, FileDisplayModel
from typing import List
import random
import string
import shutil

router = APIRouter(
    prefix="/file",
    tags=["file"]
)


tipo_url = ["absolut", "relative"]


@router.post("/create_file", response_model=FileDisplayModel)
async def create_file(request: FileBaseModel, db: Session = Depends(get_db)):
    if not request.tipo_url in tipo_url:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter tipo_url is not valid only absolut or relative")
    return db_file.CrudFile.create_file(db, request)


@router.get("/get_all", response_model=List[FileDisplayModel])
async def get_all(db: Session = Depends(get_db)):
    return db_file.CrudFile.get_all(db)


@router.post("/uploadfile/")
async def upload_file(upload_file: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(upload_file.filename.rsplit('.', 1))
    path = f'./files/images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return {"filename": path}