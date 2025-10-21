from dotenv import load_dotenv
from fastapi import FastAPI

from app.aplicacion.controlador import controlador, ControladorTareaProgramada
from app.dominio.TareasAutomaticas import TareasAutomaticas

load_dotenv()

app = FastAPI()  # inicializa la aplicación

app.include_router(controlador.router)
app.include_router(ControladorTareaProgramada.router)

tareasAutomatica = TareasAutomaticas()
tareasAutomatica.iniciarTareasAutomaticas()
