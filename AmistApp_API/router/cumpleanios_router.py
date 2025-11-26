from fastapi import APIRouter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from codigo.cumpleanios import Cumpleanios
from codigo.recordatorio import Recordatorio
from codigo.sistema_amistapp import Sistema_amistapp

router = APIRouter()
sistema = Sistema_amistapp()

# ENDPOINT 1: Crear un cumpleaños
@router.post("/")
def crear_cumpleanios(
    titulo: str,
    fecha: str,
    descripcion: str,
    mensaje_felicitaciones: str,
    recordatorio_mensaje: str,
    recordatorio_fecha: str
):
    recordatorio = Recordatorio(recordatorio_mensaje, recordatorio_fecha)
    cumple = Cumpleanios(
        titulo=titulo,
        fecha=fecha,
        descripcion=descripcion,
        recordatorio=recordatorio,
        mensaje_felicitaciones=mensaje_felicitaciones
    )
    sistema.agregar_cumpleanios(cumple)
    
    return {
        "mensaje": "Cumpleaños creado exitosamente",
        "titulo": cumple.titulo,
        "fecha": cumple.fecha,
        "mensaje": cumple.mensaje_felicitaciones
    }

# ENDPOINT 2: Ver todos los cumpleaños
@router.get("/")
def ver_cumpleanios():
    cumples_lista = []
    
    for cumple in sistema.cumpleanios:
        cumples_lista.append({
            "titulo": cumple.titulo,
            "fecha": cumple.fecha,
            "descripcion": cumple.descripcion,
            "mensaje_felicitaciones": cumple.mensaje_felicitaciones,
            "dias_restantes": cumple.dias_restantes()
        })
    
    return {"cumpleaños": cumples_lista}