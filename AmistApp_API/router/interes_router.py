

from fastapi import APIRouter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from codigo.interes import Interes
from codigo.sistema_amistapp import Sistema_amistapp

router = APIRouter()
sistema = Sistema_amistapp()

# ENDPOINT 1: Crear un interés
@router.post("/")
def crear_interes(nombre: str, descripcion: str, categoria: str, nivel_frecuencia: int):
    interes = Interes(nombre, descripcion, categoria, nivel_frecuencia)
    sistema.agregar_interes(interes)
    
    return {
        "mensaje": "Interés creado exitosamente",
        "nombre": interes.nombre,
        "categoria": interes.categoria
    }

# ENDPOINT 2: Ver todos los intereses
@router.get("/")
def ver_intereses():
    intereses_lista = []
    
    for interes in sistema.intereses:
        intereses_lista.append({
            "nombre": interes.nombre,
            "descripcion": interes.descripcion,
            "categoria": interes.categoria,
            "nivel_frecuencia": interes.nivel_frecuencia
        })
    
    return {"intereses": intereses_lista}

# ENDPOINT 3: Ver categorías disponibles
@router.get("/categorias")
def ver_categorias():
    return {"categorias": list(Interes.CATEGORIAS_VALIDAS)}