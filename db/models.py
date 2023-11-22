from db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# MODELO DE DEFINICION DE LA TABLA DE LA BASE DE DATOS
#  es la estructura de la tabla

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base



class Documento(Base):
    __tablename__ = "documento"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tipo = Column(String)
    tamaño = Column(Integer)
    acceso = Column(Boolean)
    propietario = Column(String)

    carpetas = relationship("Carpeta", back_populates="documento")
    rutas = relationship("Ruta", back_populates="documento")
    accesos = relationship("Acceso", back_populates="documento")
    registros_acceso = relationship("Registro", back_populates="documento")

class Carpeta(Base):
    __tablename__ = "carpeta"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    elementos = Column(String)

    documento_id = Column(Integer, ForeignKey("documento.id"))
    documento = relationship("Documento", back_populates="carpetas")

class Ruta(Base):
    __tablename__ = "ruta"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    destino = Column(String)

    documento_id = Column(Integer, ForeignKey("documento.id"))
    documento = relationship("Documento", back_populates="rutas")

class Acceso(Base):
    __tablename__ = "acceso"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tipo = Column(String)

    documento_id = Column(Integer, ForeignKey("documento.id"))
    documento = relationship("Documento", back_populates="accesos")

class Registro(Base):
    __tablename__ = "registro"

    id = Column(Integer, primary_key=True)
    # Otras columnas de registro...

    documento_id = Column(Integer, ForeignKey("documento.id"))
    documento = relationship("Documento", back_populates="registros_acceso")
