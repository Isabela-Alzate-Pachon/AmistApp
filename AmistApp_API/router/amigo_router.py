from fastapi import APIRouter
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from codigo.amigo import Amigo
from codigo.sistema_amistapp import Sistema_amistapp

router = APIRouter()
sistema = Sistema_amistapp()

# ENDPOINT 1: Crear un amigo
@router.post("/")
def crear_amigo(nombre: str, apellido: str, apodo: str, genero: str):
    amigo = Amigo(nombre, apellido, apodo, genero)
    sistema.agregar_amigo(amigo)
    
    return {
        "mensaje": "Amigo creado exitosamente",
        "nombre": amigo.nombre,
        "apellido": amigo.apellido,
        "apodo": amigo.apodo,
        "genero": amigo.genero
    }

# ENDPOINT 2: Ver todos los amigos
@router.get("/")
def ver_amigos():
    amigos_lista = []
    
    for amigo in sistema.amigos:
        amigos_lista.append({
            "nombre": amigo.nombre,
            "apellido": amigo.apellido,
            "apodo": amigo.apodo,
            "genero": amigo.genero
        })
    
    return {"amigos": amigos_lista}

# ENDPOINT 3: Buscar un amigo por nombre
@router.get("/{nombre}")
def buscar_amigo(nombre: str):
    amigo = sistema.buscar_amigo(nombre)
    
    if amigo:
        return {
            "nombre": amigo.nombre,
            "apellido": amigo.apellido,
            "apodo": amigo.apodo,
            "genero": amigo.genero
        }
    else:
        return {"mensaje": "Amigo no encontrado"}