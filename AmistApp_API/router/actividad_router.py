

from fastapi import APIRouter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from codigo.actividad import Actividad
from codigo.recordatorio import Recordatorio
from codigo.sistema_amistapp import Sistema_amistapp

router = APIRouter()
sistema = Sistema_amistapp()

# ENDPOINT 1: Crear una actividad
@router.post("/")
def crear_actividad(titulo: str, fecha: str, descripcion: str, recordatorio_mensaje: str, recordatorio_fecha: str):
    recordatorio = Recordatorio(recordatorio_mensaje, recordatorio_fecha)
    actividad = Actividad(titulo, fecha, descripcion, recordatorio)
    sistema.agregar_actividad(actividad)
    
    return {
        "mensaje": "Actividad creada exitosamente",
        "titulo": actividad.titulo,
        "fecha": actividad.fecha
    }

# ENDPOINT 2: Ver todas las actividades
@router.get("/")
def ver_actividades():
    actividades_lista = []
    
    for act in sistema.actividades:
        if hasattr(act, 'titulo'):
            actividades_lista.append({
                "titulo": act.titulo,
                "fecha": act.fecha,
                "descripcion": act.descripcion
            })
    
    return {"actividades": actividades_lista}

# ENDPOINT 3: Eliminar una actividad
@router.delete("/{titulo}")
def eliminar_actividad(titulo: str):
    sistema.eliminar_actividad(titulo)
    return {"mensaje": f"Actividad '{titulo}' eliminada"}