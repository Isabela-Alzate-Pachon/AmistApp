from pydantic import BaseModel


class AmigoCreate(BaseModel):
    nombre: str
    apellido: str
    apodo: str
    genero: str


class AmigoResponse(BaseModel):
    nombre: str
    apellido: str
    apodo: str
    genero: str
