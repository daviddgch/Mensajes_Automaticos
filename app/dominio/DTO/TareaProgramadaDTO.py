from dataclasses import dataclass


@dataclass
class TareaProgramadaDTO:
    id: str = ""

    hora: int = 0
    minuto: int = 0
    segundo: int = 0
    dia: int = 0
    mes: int = 0
    anos: int = 0
