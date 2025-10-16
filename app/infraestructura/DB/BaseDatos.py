import json
import os
from dataclasses import asdict

from app.dominio.DTO.DestinatarioDTO  import DestinatarioDTO
from app.infraestructura.DB.ABaseDatos import ABaseDatos


class BaseDatos(ABaseDatos):

    def __init__(self):
        if not os.path.exists("Base_De_Datos"):
            with open("Base_De_Datos", "w", encoding="utf-8") as f:
                f.write("")

    def agregarDestinatarioBD(self, destinatario):
        #lista_json = [
        #    {"id": 1, "nombre": "Juan", "numero": "12345"},
        #    {"id": 2, "nombre": "María", "numero": "67890"},
        #    {"id": 3, "nombre": "Carlos", "numero": "54321"}
        #]

        destinatarios = self.obtenerTodosDestinatarios()
        destinatarios.append(destinatario)

        destinatarioJson = [asdict(d) for d in destinatarios]
        with open("Base_De_Datos", "w", encoding="utf-8") as f:
            json.dump(destinatarioJson, f, ensure_ascii=False, indent=4)

    def obtenerTodosDestinatarios(self):
        with open("Base_De_Datos", "r", encoding="ut/-8") as f:
            destinatariosJson = json.loads(f.read())
            destinatarios = [DestinatarioDTO(**destinatariosJson) for destinatariosJson in destinatariosJson]

            return destinatarios
