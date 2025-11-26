from pydantic import BaseModel
from recordatorio_schema import RecordatorioCreate

# Schema para crear un evento
class EventoCreate(BaseModel):
    titulo: str
    fecha: str
    descripcion: str
    lugar: str
    duracion: float
    nivel_importancia: int
    estado: str
    recordatorio: RecordatorioCreate

# Schema para mostrar un evento
class EventoResponse(BaseModel):
    titulo: str
    fecha: str
    descripcion: str
    lugar: str
    duracion: float
    nivel_importancia: int
    estado: str