

from fastapi import APIRouter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from codigo.recordatorio import Recordatorio

router = APIRouter()
recordatorios = []

# ENDPOINT 1: Crear un recordatorio
@router.post("/")
def crear_recordatorio(mensaje: str, fecha: str):
    recordatorio = Recordatorio(mensaje, fecha)
    recordatorios.append(recordatorio)
    
    return {
        "mensaje": "Recordatorio creado exitosamente",
        "recordatorio_mensaje": recordatorio.mensaje,
        "fecha": recordatorio.fecha
    }

# ENDPOINT 2: Ver todos los recordatorios
@router.get("/")
def ver_recordatorios():
    recordatorios_lista = []
    
    for rec in recordatorios:
        recordatorios_lista.append({
            "mensaje": rec.mensaje,
            "fecha": rec.fecha
        })
    
    return {"recordatorios": recordatorios_lista}