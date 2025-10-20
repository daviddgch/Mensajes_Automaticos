from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import APIRouter, Request

from app.aplicacion.SchedulerConfiguracion import scheduler
from app.dominio.DTO.TareaProgramadaDTO import TareaProgramadaDTO
from app.dominio.TareasAutomaticas import TareasAutomaticas

router = APIRouter()
tareasAutomatica = TareasAutomaticas()



# --- ENDPOINTS ---

@router.post("/scheduler/start")
async def iniciar_scheduler():
    if not tareasAutomatica.estaCorriendo():
        tareasAutomatica.iniciarTareasAutomaticas()
        return {"ok": True, "message": "Scheduler iniciado."}
    return {"ok": False, "message": "El scheduler ya estaba en ejecución."}

@router.post("/scheduler/stop")
async def detener_scheduler():
    if tareasAutomatica.estaCorriendo():
        tareasAutomatica.pararTareasAutomaticas()
        return {"ok": True, "message": "Scheduler detenido."}
    return {"ok": False, "message": "El scheduler no está en ejecución."}

@router.post("/scheduler/agregar")
async def agregar_scheduler(request: Request):
    data = await request.json()

    if tareasAutomatica.estaCorriendo():
        tareaProgramadaDto = TareaProgramadaDTO(**data)
        print(tareaProgramadaDto)
        tareasAutomatica.agregarTareaAutomaticas(tareaProgramadaDto)
        return {"ok": True, "message": "Tarea agregada."}
    return {"ok": False, "message": "El scheduler no está en ejecución."}

@router.get("/scheduler/status")
async def estado_scheduler():
    estaCorriendo = tareasAutomatica.estaCorriendo()
    return {
        "running": estaCorriendo,
        "jobs": [job.id for job in scheduler.get_jobs()] if estaCorriendo else []
    }