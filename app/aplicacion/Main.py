from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from app.aplicacion.controlador import controlador, ControladorTareaProgramada
from app.dominio.ProcesamientoMensajeria import ProcesamientoMensajeria

app = FastAPI()  # inicializa la aplicación

scheduler = BackgroundScheduler()

tareaAutomatica = ProcesamientoMensajeria()
scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=11, minute=11, second=4, misfire_grace_time=10, id="11am")
scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=23, minute=11, second=4, misfire_grace_time=10, id="11pm")
#scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=21, minute=44, second=0, misfire_grace_time=10, id="12pm")
scheduler.start()
app.include_router(controlador.router)
app.include_router(ControladorTareaProgramada.router)