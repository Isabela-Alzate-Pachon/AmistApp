from .recordatorio import Recordatorio

class Actividad:
    def __init__(self, titulo, fecha, descripcion, recordatorio):
        self.titulo = titulo
        self.fecha = fecha
        self.descripcion = descripcion
        self.recordatorio = recordatorio

       
       
    
    def mostrar_actividad(self):
        print(f"\n📅 Actividad: {self.titulo}")
        print(f"🗓️ Fecha: {self.fecha}")
        print(f"📝 Descripción: {self.descripcion}")
        print(f"⏰ Recordatorio: '{self.recordatorio.mensaje}' programado para {self.recordatorio.fecha}")

        if self.recordatorio:
            print(f"⏰ Recordatorio: '{self.recordatorio.mensaje}' programado para {self.recordatorio.fecha}")
        else:
            print("⏰ No hay recordatorio asignado.")    