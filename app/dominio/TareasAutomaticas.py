from datetime import datetime

from app.dominio.ATareasAutomaticas import ATareasAutomaticas
from app.aplicacion.SchedulerConfiguracion import scheduler
from app.dominio.DTO.TareaProgramadaDTO import TareaProgramadaDTO
from app.dominio.ProcesamientoMensajeria import ProcesamientoMensajeria


class TareasAutomaticas(ATareasAutomaticas):
    tareaAutomatica = ProcesamientoMensajeria()

    def iniciarTareasAutomaticas(self):
        scheduler.add_job(self.tareaAutomatica.enviarMensaje, "cron", hour=11, minute=11, second=4, misfire_grace_time=10,
                          id="11am")
        scheduler.add_job(self.tareaAutomatica.enviarMensaje, "cron", hour=23, minute=11, second=4, misfire_grace_time=10,
                          id="11pm")
        scheduler.start()


    def pararTareasAutomaticas(self):
        scheduler.shutdown(wait=False)

    def estaCorriendo(self):
        return scheduler.running

    def agregarTareaAutomaticas(self, tareaProgramada: TareaProgramadaDTO):
        scheduler.add_job(
            self.tareaAutomatica.enviarMensaje,
            trigger="date",
            run_date=datetime(tareaProgramada.anos,
                              tareaProgramada.mes,
                              tareaProgramada.dia,
                              tareaProgramada.hora,
                              tareaProgramada.minuto,
                              tareaProgramada.segundo),  # año, mes, día, hora, min, seg
            id=tareaProgramada.id
        )
