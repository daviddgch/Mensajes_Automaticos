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
        if not os.path.exists("Base_De_Datos_Mensajes"):
            with open("Base_De_Datos_Mensajes", "w", encoding="utf-8") as f:
                f.write("")

    def agregarDestinatarioBD(self, destinatario):

        destinatarios = self.obtenerTodosDestinatarios()
        destinatarios.append(destinatario)

        destinatarioJson = [asdict(d) for d in destinatarios]
        with open("Base_De_Datos", "w", encoding="utf-8") as f:
            json.dump(destinatarioJson, f, ensure_ascii=False, indent=4)

    def agregarMensajeBD(self, mensajeNuevo):
        mensajes = self.obtenerMensajes()
        mensajes.append(mensajeNuevo)
        with open("Base_De_Datos_Mensajes", "w", encoding="utf-8") as f:
            json.dump(mensajes, f, ensure_ascii=False, indent=4)

    def obtenerTodosDestinatarios(self):
        destinatarios = []
        try:
            with open("Base_De_Datos", "r", encoding="utf-8") as f:
                destinatariosJson = json.loads(f.read())
                destinatarios = [DestinatarioDTO(**destinatariosJson) for destinatariosJson in destinatariosJson]
                return destinatarios
        except Exception as e:
            print(e)
            return destinatarios

    def obtenerMensajes(self):
        mensajes = []
        try:
            with open("Base_De_Datos_Mensajes", "r", encoding="utf-8") as f:
                mensajes = json.loads(f.read())
                return mensajes
        except Exception as e:
            print(e)
            return mensajes

    def borrarDestinatario(self, destinatario):
        destinatarios = self.obtenerTodosDestinatarios()
        try:
            for destinatarioBD in destinatarios:
                if destinatarioBD.nombre == destinatario.nombre or destinatarioBD.numero == destinatario.numero:
                    destinatarios.remove(destinatarioBD)

            destinatarioJson = [asdict(d) for d in destinatarios]
            with open("Base_De_Datos", "w", encoding="utf-8") as f:
                json.dump(destinatarioJson, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)
            return "Error en borrar destinatario"

    def borrarMensaje(self, mensaje):
        mensajes = self.obtenerMensajes()
        try:
            mensajes.remove(mensaje)
            with open("Base_De_Datos_Mensajes", "w", encoding="utf-8") as f:
                json.dump(mensajes, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(e)
            return "Error en borrarMensaje"
