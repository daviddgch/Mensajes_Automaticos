from app.dominio.AModificacionDestinatario import AModificacionDestinatario
from app.dominio.DTO.DestinatarioDTO import  DestinatarioDTO
from app.infraestructura.DB.BaseDatos import BaseDatos


class ModificacionDestinatario(AModificacionDestinatario):

    def __init__(self):
        self.baseDatos = BaseDatos()
        pass

    def agregarDestinatario(self, destinatario: DestinatarioDTO):
        self.baseDatos.agregarDestinatarioBD(destinatario)
        print("Agregado a destinatario")
        return True

    def agregarMensaje(self, mensajeNuevo):
        self.baseDatos.agregarMensajeBD(mensajeNuevo)
        pass

    def obtenerTodosDestinatarios(self):
        return self.baseDatos.obtenerTodosDestinatarios()

    def obtenerMensajes(self):
        return self.baseDatos.obtenerMensajes()

    def borrarDestinatario(self, destinatario: DestinatarioDTO):
        self.baseDatos.borrarDestinatario(destinatario)

    def borrarMensaje(self, mensaje):
        self.baseDatos.borrarMensaje(mensaje)

