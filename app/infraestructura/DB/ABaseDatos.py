from abc import abstractmethod

from app.dominio.DTO import DestinatarioDTO


class ABaseDatos:

    @abstractmethod
    def agregarDestinatarioBD(destinatario : DestinatarioDTO):
        pass
