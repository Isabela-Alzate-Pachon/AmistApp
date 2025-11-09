from recordatorio import Recordatorio 

class Actividad:
    def __init__(self, titulo:str,fecha:str, descripcion: str, mensaje_recordatorio: str, fecha_recordatorio: str):
       self.titulo = titulo
       self.fecha = fecha 
       self.descripcion = descripcion 
       
       self.recordatorio = Recordatorio(mensaje_recordatorio, fecha_recordatorio)
    
    def mostrar_actividad(self):
        print(f"\n📅 Actividad: {self.titulo}")
        print(f"🗓️ Fecha: {self.fecha}")
        print(f"📝 Descripción: {self.descripcion}")
        print(f"⏰ Recordatorio: '{self.recordatorio.mensaje}' programado para {self.recordatorio.fecha}")
        