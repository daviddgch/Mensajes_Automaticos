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

