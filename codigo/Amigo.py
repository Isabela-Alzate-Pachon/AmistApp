
class Amigo:
    def __init__(self, nombre: str, apellido: str, apodo: str, genero: str):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.genero = genero
        self.intereses: list[Intereses] = []
        self.recordatorio: list[Recordatorio] = []
        
    