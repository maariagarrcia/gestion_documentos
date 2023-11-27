from abc import ABC, abstractmethod
from db.models import DbCarpeta, DbFile
from schemas import User, CarpetaDisplayModel
from sqlalchemy.orm import Session
from composite import Archivo, Carpeta
from db import db_carpeta


class CrudCarpetaInterface(ABC):
    @abstractmethod
    def create_carpeta(db, carpeta):
        pass

    @abstractmethod
    def get_carpeta(db, id):
        pass

    @abstractmethod
    def get_all_carpeta(db):
        pass

    @abstractmethod
    def update_carpeta(db, id, carpeta):
        pass

    @abstractmethod
    def delete_carpeta(db, id):
        pass


class CrudCarpeta(CrudCarpetaInterface):
    @staticmethod
    def create_carpeta(db, request):
        new_carpeta = DbCarpeta(nombre=request.nombre,
                                tamaño=request.tamaño, user_id=request.user_id)

        userr = User(id=request.user_id, username=" ")

        for nombre_archivo in request.archivos:
            archivo = DbFile(nombre=nombre_archivo)
            new_carpeta.archivos.append(archivo)

        db.add(new_carpeta)
        db.commit()
        db.refresh(new_carpeta)
        new_carpeta = CarpetaDisplayModel(nombre=new_carpeta.nombre, tamaño=new_carpeta.tamaño, user=userr, archivos=[
                                          archivo.nombre for archivo in new_carpeta.archivos])
        
        return new_carpeta

    @staticmethod
    def get_carpeta(db: Session, id: int):
        carpeta = db.query(DbCarpeta).filter(DbCarpeta.id == id).first()
        archivos = [archivo.nombre for archivo in carpeta.archivos]
        userr = User(id=carpeta.user_id, username=" ")
        carpeta = CarpetaDisplayModel(
            id=carpeta.id,nombre=carpeta.nombre, tamaño=carpeta.tamaño, user=userr, archivos=archivos)
        return carpeta
    
    @staticmethod
    def get_carpeta_comp(db: Session, id: int):
        pass
    @staticmethod
    def get_all_carpeta(db: Session):
        carpetas = db.query(DbCarpeta).all()
        carpetas = [CarpetaDisplayModel(id=carpeta.id,nombre=carpeta.nombre, tamaño=carpeta.tamaño, user=User(id=carpeta.user_id, username=" "), archivos=[
                                        archivo.nombre for archivo in carpeta.archivos]) for carpeta in carpetas]
        return carpetas

    @staticmethod
    def update_carpeta(db, id, request):
        carpeta = db.query(DbCarpeta).filter(DbCarpeta.id == id).first()
        carpeta.nombre = request.nombre
        carpeta.tamaño = request.tamaño
        carpeta.elementos = request.elementos
        db.commit()
        db.refresh(carpeta)
        return carpeta

    @staticmethod
    def delete_carpeta(db, id):
        carpeta = db.query(DbCarpeta).filter(DbCarpeta.id == id).first()
        db.delete(carpeta)
        db.commit()
        return True
