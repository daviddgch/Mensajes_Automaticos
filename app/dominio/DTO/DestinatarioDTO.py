from dataclasses import dataclass


@dataclass
class DestinatarioDTO:

    id: int
    nombre: str
    numero: str

    def __init__(self, id, nombre, numero):
        self.id = id
        self.nombre = nombre
        self.numero = numero