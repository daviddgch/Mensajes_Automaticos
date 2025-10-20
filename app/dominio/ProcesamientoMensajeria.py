from app.dominio.AProcesamientoMensajeria import AProcesamientoMensajeria
from app.infraestructura.DB.BaseDatos import BaseDatos
from app.infraestructura.mensajeria.ServicioMensajeria import ServicioMensajeria


class ProcesamientoMensajeria(AProcesamientoMensajeria):

    mensajePredeterminado = "11:11"

    servicioMensajeria = ServicioMensajeria()
    baseDatos = BaseDatos()

    def enviarMensaje(self):
        destinatarios = self.baseDatos.obtenerTodosDestinatarios()
        mensajes = self.baseDatos.obtenerMensajes()
        mensajes = self.baseDatos.obtenerMensajes()[0] if len(mensajes) > 0 else self.mensajePredeterminado

        print(mensajes)
        print(destinatarios)

        for destinatario in destinatarios:
            self.servicioMensajeria.enviarPorMensajeria(destinatario.numero, mensajes)

        self.baseDatos.borrarMensaje(mensajes)
        print("Mensaje enviada")