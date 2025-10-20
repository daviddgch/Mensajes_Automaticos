from abc import abstractmethod

from app.dominio.DTO import DestinatarioDTO


class ABaseDatos:

    @abstractmethod
    def agregarDestinatarioBD(destinatario : DestinatarioDTO):
        pass

    @abstractmethod
    def agregarMensajeBD(self, mensajeNuevo):
        pass

    @abstractmethod
    def obtenerTodosDestinatarios(self):
        pass

    @abstractmethod
    def obtenerMensajes(self):
        pass

    @abstractmethod
    def borrarDestinatario(self, destinatario):
        pass

    @abstractmethod
    def borrarMensaje(self, mensaje):
        pass
