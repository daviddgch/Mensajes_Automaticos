from abc import abstractmethod

from app.dominio.DTO import DestinatarioDTO


class  AModificacionDestinatario:

    @abstractmethod
    def agregarDestinatario(self, destinatario: DestinatarioDTO):
        pass