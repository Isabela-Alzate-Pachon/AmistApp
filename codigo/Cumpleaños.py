from datetime import datetime
from Actividad import Actividad
from Recordatorio import Recordatorio

class Cumpleaños(Actividad):
    def __init__(self, titulo:str, fecha:str, descripcion: str, recordatorio: Recordatorio, mensaje_felicitaciones: str):
        super().__init__(titulo, fecha, descripcion, recordatorio)
        self.mensaje_felicitaciones = mensaje_felicitaciones
    
    def dias_restantes(self)-> int:
        try:
            fecha_evento = datetime.strptime(self.fecha,"%Y-%m-%d" )
            hoy = datetime.now()
            diferencia = (fecha_evento -hoy).days
            return diferencia if diferencia >= 0 else 0
        except ValueError:
            print("⚠️ Formato de fecha inválido. Usa AAAA-MM-DD.")
            return -1
    
    def mostrar_actividad(self):
        dias = self.dias_restantes()
        print (f"🎂 Cumpleaños: {self.titulo}\n"
                f"📅 Fecha: {self.fecha}\n"
                f"📝 Descripción: {self.descripcion}\n"
                f"💌 Mensaje de felicitación: {self.mensaje_felicitaciones}\n"
                f"⏳ Días restantes: {dias}\n"
                f"⏰ Recordatorio: {self.recordatorio.mensaje} ({self.recordatorio.fecha})")
    