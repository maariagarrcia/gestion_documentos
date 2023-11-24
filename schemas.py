from pydantic import BaseModel
from typing import List
from datetime import datetime

class UserBaseModel(BaseModel):
    username: str
    email: str
    hashed_password: str

class UserDisplayModel(BaseModel):
    username: str
    class Config():
        orm_mode = True


class User(BaseModel):
    id: int
    username: str
 
    class Config():
        orm_mode = True

class FileBaseModel(BaseModel):
    nombre:str 
    tamaño:int
    url:str
    tipo_url:str
    user_id:int
    carpeta_id:int

class FileDisplayModel(BaseModel):
    id:int
    nombre:str
    tamaño:int
    url:str
    tipo_url:str
    user: User
    carpeta_id:int

    class Config():
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str


class CarpetaBaseModel(BaseModel):
    nombre:str 
    tamaño:int
    user_id:int
    archivos: List[str] = []


class CarpetaDisplayModel(BaseModel):
    id:int
    nombre:str
    tamaño:int
    user: User
    archivos: List[str] = []

    class Config():
        orm_mode = True