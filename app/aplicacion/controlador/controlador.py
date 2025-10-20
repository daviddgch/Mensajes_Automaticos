from fastapi import APIRouter, Request
from app.dominio.DTO.DestinatarioDTO import  DestinatarioDTO
from app.dominio.ModificacionDestinatario import ModificacionDestinatario

router = APIRouter()

_modificacionDestinatario = ModificacionDestinatario()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/agregarDestinatario")
async def agregarDestinatario(request: Request):
    data = await request.json()
    destinatarioDTO = DestinatarioDTO(**data)
    _modificacionDestinatario.agregarDestinatario(destinatarioDTO)
    return {"ok":True}

@router.post("/agregarMensaje")
async def agregarMensaje(request: Request):
    data = await request.json()
    mensaje = data["mensaje"]
    _modificacionDestinatario.agregarMensaje(mensaje)
    return {"ok":True}

@router.get("/obtenerDestinatarios")
async def obtenerDestinatarios():
        return _modificacionDestinatario.obtenerTodosDestinatarios()

@router.get("/obtenerMensajes")
async def obtenerMensajes():
    return _modificacionDestinatario.obtenerMensajes()

@router.delete("/borrarDestinatario")
async def borrarDestinatario(request: Request):
    data = await request.json()

    destinatarioDTO = DestinatarioDTO(**data)
    _modificacionDestinatario.borrarDestinatario(destinatarioDTO)
    return {"ok":True}

@router.delete("/borrarMensaje")
async def borrarMensaje(request: Request):
    data = await request.json()
    mensaje = data["mensaje"]
    _modificacionDestinatario.borrarMensaje(mensaje)
    return {"ok":True}
