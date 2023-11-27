import uvicorn

from fastapi import FastAPI, Request
from fastapi import FastAPI, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from db import models
from db.database import engine


from router import file, user,carpeta
from auth import authentication

from fastapi.responses import JSONResponse

from schemas import RegistroClic
from proxy import *




app = FastAPI()
app.include_router(carpeta.router)
app.include_router(user.router)
app.include_router(file.router)
app.include_router(authentication.router)                                               


app.mount("/static/css/", StaticFiles(directory="static/css"), name="static")

app.mount("/files/images", StaticFiles(directory="files/images"), name="files")

app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


def guardar_en_archivo(info):
    with open("registros_clic.txt", "a") as archivo:
        archivo.write(info + "\n")

@app.post("/registrar_clic")
async def registrar_clic(registro: RegistroClic):
    try:
        # Formatear la información
        info = f"User ID: {registro.user_id}, Elemento: {registro.elemento}, Tipo: {registro.tipo}"

        # Guardar la información usando el proxy
        proxy_guardador.guardar(info)

        return {"message": "Clic registrado con éxito"}
    except Exception as e:
        return {"error": str(e)}

models.Base.metadata.create_all(engine)


if __name__ == "__main__":
    print("-> Inicio integrado de servicIo web")
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    print("=> Iniciado desde el servidor web")
    print("   Módulo python iniciado:", __name__)

