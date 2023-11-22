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
    username: str
 
    class Config():
        orm_mode = True

class FileBaseModel(BaseModel):
    nombre:str 
    tamaño:int
    url:str
    tipo_url:str
    user_id:int

class FileDisplayModel(BaseModel):
    id:int
    nombre:str
    tamaño:int
    url:str
    tipo_url:str
    user: User

    class Config():
        orm_mode = True

