from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI

from app.aplicacion.controlador import controlador
from app.dominio.ProcesamientoMensajeria import ProcesamientoMensajeria

app = FastAPI()  # inicializa la aplicación

scheduler = BackgroundScheduler()

tareaAutomatica = ProcesamientoMensajeria()
scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=11, minute=11, second=4)
scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=23, minute=11, second=4)
scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=0, minute=43, second=0)
scheduler.start()
app.include_router(controlador.router)