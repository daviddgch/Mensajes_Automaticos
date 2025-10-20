from fastapi import FastAPI
from app.aplicacion.SchedulerConfiguracion import scheduler
from app.aplicacion.controlador import controlador, ControladorTareaProgramada
from app.aplicacion.controlador.ControladorTareaProgramada import scheduler
from app.dominio.ProcesamientoMensajeria import ProcesamientoMensajeria
from app.dominio.TareasAutomaticas import TareasAutomaticas

app = FastAPI()  # inicializa la aplicación

app.include_router(controlador.router)
app.include_router(ControladorTareaProgramada.router)

tareasAutomatica = TareasAutomaticas()
tareasAutomatica.iniciarTareasAutomaticas()

"""tareaAutomatica = ProcesamientoMensajeria()
scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=11, minute=11, second=4, misfire_grace_time=10, id="11am")
scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=23, minute=11, second=4, misfire_grace_time=10, id="11pm")
#scheduler.add_job(tareaAutomatica.enviarMensaje, "cron", hour=21, minute=44, second=0, misfire_grace_time=10, id="12pm")
scheduler.start()"""


