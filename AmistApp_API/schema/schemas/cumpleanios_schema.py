from pydantic import BaseModel
from recordatorio_schema import RecordatorioCreate

# Schema para crear un cumpleaños
class CumpleaniosCreate(BaseModel):
    titulo: str
    fecha: str
    descripcion: str
    mensaje_felicitaciones: str
    recordatorio: RecordatorioCreate

# Schema para mostrar un cumpleaños
class CumpleaniosResponse(BaseModel):
    titulo: str
    fecha: str
    descripcion: str
    mensaje_felicitaciones: str
    dias_restantes: int