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

