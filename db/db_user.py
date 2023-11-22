from sqlalchemy.orm.session import Session
from schemas import UserBaseModel
from db.models import DbUser
from db.hash import Hash
from fastapi import HTTPException
from schemas import UserDisplayModel

from abc import ABC, abstractmethod


# CRUD DE USER
class CrudUserInterfaz(ABC):
    @abstractmethod
    def create_user(self, data,request):
        # create a new record in the database
        pass

    @abstractmethod
    def get_all(self,data,request):
        # get all records from the database
        pass

    @abstractmethod
    def get_user_by_username(self, username, data):
        # get a record from the database
        pass

    @abstractmethod
    def update_user(self, id, data,request):
        # update a record in the database
        pass

    @abstractmethod
    def delete_user(self, id, data):
        # delete a record from the database
        pass


class CrudUser(CrudUserInterfaz):
    @staticmethod
    def create_user(db: Session, request: UserBaseModel):
        new_user = DbUser(
            username=request.username,
            email=request.email,
            hashed_password=Hash.bcrypt(request.hashed_password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def get_all(db: Session):
        users = db.query(DbUser).all()
        return users
    
    @staticmethod
    def get_user_by_username(username: str, db: Session):
        user = db.query(DbUser).filter(DbUser.username == username).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
         
    @staticmethod
    def update_user(id:int, request:UserBaseModel, db: Session):
        user = db.query(DbUser).filter(DbUser.id == id).first()
        if user:
            # Actualiza los datos del usuario con la información de 'request'.
            user.username = request.username
            user.email = request.email
            user.hashed_password = request.hashed_password
            db.commit()
            return UserDisplayModel(
                id=user.id,
                username=user.username,
                email=user.email
            )
        else:
            raise HTTPException(status_code=404, detail="User not found")
        
    @staticmethod
    def delete_user(id:int, db: Session):
        user = db.query(DbUser).filter(DbUser.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        return "ok"

    
