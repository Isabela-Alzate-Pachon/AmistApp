from actividad import Actividad
from recordatorio import Recordatorio

class Evento(Actividad):
    def __init__(self, fecha: str, recordatorio: Recordatorio, lugar:str, duracion: float, nivel_importancia: int, estado: str):
        super().__init__(fecha, recordatorio)
        
        self.lugar = lugar
        self.duracion = duracion 
        self.nivel_importancia = nivel_importancia
        self.estado = estado
        
    def mostrar_importancia(self) -> str:
        if 1<= self.nivel_importancia <=3:
            return "🤏Baja"
        elif 4<= self.nivel_importancia <=7:
            return "🫣Media"
        elif 8 <= self.nivel_importancia <= 10:
            return "🫡Alta"
        else:
            return "valor no valido"
    
    def mostrar_actividad(self):
        print(f"n🎉 Evento programado:")
        print(f"📍 Lugar: {self.lugar}")
        print(f"⏱️ Duración: {self.duracion} horas")
        print(f"🔥 Importancia: {self.mostrar_importancia()} ({self.nivel_importancia}/10)")
        print(f"📅 Fecha: {self.fecha}")
        print(f"📌 Estado: {self.estado}")
        print(f"⏰ Recordatorio: {self.recordatorio.mensaje} - Fecha recordatorio: {self.recordatorio.fecha}")
        