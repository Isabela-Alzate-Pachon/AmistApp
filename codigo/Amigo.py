from .interes import Interes
from .recordatorio import Recordatorio


class Amigo:
    def __init__(self, nombre: str, apellido: str, apodo: str, genero: str):
        self.nombre = nombre
        self.apellido = apellido
        self.apodo = apodo
        self.genero = genero
        self.intereses: list[Interes] = []
        self.recordatorios: list[Recordatorio] = []
    
    
    def mostrar_info(self):
        print(f"🫂Amigo: {self.nombre} {self.apellido} ({self.apodo}) - Género: {self.genero}") 
        
        if self.intereses:
            print("   ⭐ Intereses:")
            for interes in self.intereses:
                print(f"      - {interes.nombre}")
        else:
            print("   ❗ No tiene intereses registrados.")
            
            
        if self.recordatorios:
            print("   Recordatorios:")
            for rec in self.recordatorios:
                print(f"📅 {rec.mensaje} - {rec.fecha}")
    
    def agregar_interes(self, interes: Interes):
        self.intereses.append(interes)
        
        
    def agregar_recordatorio(self, recordatorio: Recordatorio):
        self.recordatorios.append(recordatorio)
        print(f"📎Recordatorio '{recordatorio.mensaje}' agregado a {self.nombre}.")
        