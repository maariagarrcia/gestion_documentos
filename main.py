import uvicorn

from fastapi import FastAPI, Request
from fastapi import FastAPI, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db import models
from db.database import engine


from router import file, user
from auth import authentication




app = FastAPI()
app.include_router(user.router)
app.include_router(file.router)
app.include_router(authentication.router)                                               


app.mount("/static/css/", StaticFiles(directory="static/css"), name="static")

app.mount("/files/images", StaticFiles(directory="files/images"), name="files")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return {"Bienvenido a la gestión de documentos"}

models.Base.metadata.create_all(engine)


if __name__ == "__main__":
    print("-> Inicio integrado de servicIo web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)

