
from pydantic import BaseModel
from recordatorio_schema import RecordatorioCreate  # ← SIN "schema."

# Schema para crear una actividad
class ActividadCreate(BaseModel):
    titulo: str
    fecha: str
    descripcion: str
    recordatorio: RecordatorioCreate

# Schema para mostrar una actividad
class ActividadResponse(BaseModel):
    titulo: str
    fecha: str
    descripcion: str