
from pydantic import BaseModel

# Schema para crear un interés
class InteresCreate(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    nivel_frecuencia: int

# Schema para mostrar un interés
class InteresResponse(BaseModel):
    nombre: str
    descripcion: str
    categoria: str
    nivel_frecuencia: int