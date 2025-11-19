# evento.py
from actividad import Actividad
from recordatorio import Recordatorio
from typing import Optional

class Evento(Actividad):
    def __init__(
        self,
        titulo: str,
        fecha: str,
        descripcion: str,
        recordatorio: Optional[Recordatorio],
        lugar: str,
        duracion: float,
        nivel_importancia: int,
        estado: str
    ):
        # Llamamos correctamente al constructor de la clase base (Actividad)
        super().__init__(titulo, fecha, descripcion, recordatorio)

        # Atributos propios de Evento
        self.lugar = lugar
        self.duracion = duracion
        self.nivel_importancia = nivel_importancia
        self.estado = estado

    def mostrar_importancia(self) -> str:
        if 1 <= self.nivel_importancia <= 3:
            return "🤏 Baja"
        elif 4 <= self.nivel_importancia <= 7:
            return "🫣 Media"
        elif 8 <= self.nivel_importancia <= 10:
            return "🫡 Alta"
        else:
            return "Valor no válido"

    def mostrar_actividad(self):
        print("🎉 Evento programado:")
        print(f"📍 Lugar: {self.lugar}")
        print(f"⏱️ Duración: {self.duracion} horas")
        print(f"🔥 Importancia: {self.mostrar_importancia()} ({self.nivel_importancia}/10)")
        print(f"📅 Fecha: {self.fecha}")
        print(f"📌 Estado: {self.estado}")
        if self.recordatorio:
            print(f"⏰ Recordatorio: {self.recordatorio.mensaje} - Fecha recordatorio: {self.recordatorio.fecha}")
        else:
            print("⏰ Recordatorio: (ninguno)")
            
            
            #estoy modificando algo
            #Isabela
