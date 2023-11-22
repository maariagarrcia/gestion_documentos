from schemas import FileBaseModel
from sqlalchemy.orm.session import Session
from db.models import DbFile
from fastapi import HTTPException

from abc import ABC, abstractmethod


class CrudFileInterface(ABC):
    @abstractmethod
    def create_file(db: Session, request: FileBaseModel):
        # create a new record in the db:Sessionbase
        pass

    @abstractmethod
    def get_all(db: Session, request: FileBaseModel):
        # get all records from the db:Sessionbase
        pass

    @abstractmethod
    def get_file_by_nombre(nombre, db: Session):
        # get a record from the db:Sessionbase
        pass

    @abstractmethod
    def update_file(id, db: Session, request: FileBaseModel):
        # update a record in the db:Sessionbase
        pass

    @abstractmethod
    def delete_file(id, db: Session):
        # delete a record from the db:Sessionbase
        pass


class CrudFile(CrudFileInterface):
    @staticmethod
    def create_file(db: Session, request: FileBaseModel):
        new_file = DbFile(
            nombre=request.nombre,
            tamaño=request.tamaño,
            url=request.url,
            tipo_url=request.tipo_url,
            user_id=request.user_id
        )
        db.add(new_file)
        db.commit()
        db.refresh(new_file)
        return new_file

    @staticmethod
    def get_all(db: Session):
        return db.query(DbFile).all()

    @staticmethod
    def get_file_by_nombre(nombre, db: Session):
        return db.query(DbFile).filter(DbFile.nombre == nombre).first()

    @staticmethod
    def update_file(id, db: Session, request: FileBaseModel):
        file = db.query(DbFile).filter(DbFile.id == id).first()
        if not file:
            raise HTTPException(status_code=404, detail="File not found")
        file.nombre = request.nombre
        file.tamaño = request.tamaño
        file.url = request.url
        file.tipo_url = request.tipo_url
        file.user_id = request.user_id
        db.commit()
        return file

    @staticmethod
    def delete_file(id, db: Session):
        file = db.query(DbFile).filter(DbFile.id == id).first()
        if not file:
            raise HTTPException(status_code=404, detail="File not found")
        db.delete(file)
        db.commit()
        return file
