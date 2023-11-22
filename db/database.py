from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DEFINICIÓN DE DATABASE

SQLALCHEMY_DATABASE_URL = "sqlite:///./gestions_docs.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Aqui se crea la base de datos
Base = declarative_base()

def get_db():
   db = SessionLocal()
   
   try:
       # yield es como un return pero no termina la funcion
       yield db

   finally:
       db.close()
