from abc import abstractmethod

from app.dominio.DTO import DestinatarioDTO


class  AModificacionDestinatario:

    @abstractmethod
    def agregarDestinatario(self, destinatario: DestinatarioDTO):
        pass

    @abstractmethod
    def agregarMensaje(self, mensajeNuevo):
        pass

    @abstractmethod
    def obtenerTodosDestinatarios(self):
        pass

    @abstractmethod
    def obtenerMensajes(self):
        pass

    @abstractmethod
    def borrarDestinatario(self, destinatario: DestinatarioDTO):
        pass

    @abstractmethod
    def borrarMensaje(self, mensaje):
        pass