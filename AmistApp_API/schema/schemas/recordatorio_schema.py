from pydantic import BaseModel

# Schema para crear un recordatorio
class RecordatorioCreate(BaseModel):
    mensaje: str
    fecha: str

# Schema para mostrar un recordatorio
class RecordatorioResponse(BaseModel):
    mensaje: str
    fecha: str