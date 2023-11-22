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


class DbUser(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)

    file = relationship("DbFile", back_populates="user")

    

class DbFile(Base):
    __tablename__ = "file"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    tamaño = Column(Integer)
    url = Column(String)
    tipo_url = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("DbUser", back_populates="file")

