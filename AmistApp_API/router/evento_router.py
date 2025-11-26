

from fastapi import APIRouter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from codigo.evento import Evento
from codigo.recordatorio import Recordatorio
from codigo.sistema_amistapp import Sistema_amistapp

router = APIRouter()
sistema = Sistema_amistapp()

# ENDPOINT 1: Crear un evento
@router.post("/")
def crear_evento(
    titulo: str, 
    fecha: str, 
    descripcion: str, 
    lugar: str, 
    duracion: float, 
    nivel_importancia: int, 
    estado: str,
    recordatorio_mensaje: str,
    recordatorio_fecha: str
):
    recordatorio = Recordatorio(recordatorio_mensaje, recordatorio_fecha)
    evento = Evento(
        titulo=titulo,
        fecha=fecha,
        descripcion=descripcion,
        recordatorio=recordatorio,
        lugar=lugar,
        duracion=duracion,
        nivel_importancia=nivel_importancia,
        estado=estado
    )
    sistema.agregar_actividad(evento)
    
    return {
        "mensaje": "Evento creado exitosamente",
        "titulo": evento.titulo,
        "lugar": evento.lugar,
        "fecha": evento.fecha
    }

# ENDPOINT 2: Ver todos los eventos
@router.get("/")
def ver_eventos():
    eventos_lista = []
    
    for actividad in sistema.actividades:
        if isinstance(actividad, Evento):
            eventos_lista.append({
                "titulo": actividad.titulo,
                "fecha": actividad.fecha,
                "lugar": actividad.lugar,
                "duracion": actividad.duracion,
                "importancia": actividad.nivel_importancia,
                "estado": actividad.estado
            })
    
    return {"eventos": eventos_lista}