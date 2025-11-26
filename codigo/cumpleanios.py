from datetime import datetime
from .actividad import Actividad
from .recordatorio import Recordatorio

class Cumpleanios(Actividad):
    def __init__(self, titulo: str, fecha: str, descripcion: str,
                 recordatorio: Recordatorio, mensaje_felicitaciones: str):
        
        super().__init__(titulo, fecha, descripcion, recordatorio)
        self.mensaje_felicitaciones = mensaje_felicitaciones

    def dias_restantes(self) -> int:
        try:
            fecha_evento = datetime.strptime(self.fecha, "%Y-%m-%d").date()
            hoy = datetime.now().date()
            diferencia = (fecha_evento - hoy).days
            return max(diferencia, 0)
        except ValueError:
            print("⚠️ Formato de fecha inválido. Usa AAAA-MM-DD.")
            return -1

    def mostrar_actividad(self):
        dias = self.dias_restantes()
        
        print(f"🎂 Cumpleaños: {self.titulo}")
        print(f"📅 Fecha: {self.fecha}")
        print(f"📝 Descripción: {self.descripcion}")
        print(f"💌 Mensaje de felicitación: {self.mensaje_felicitaciones}")
        print(f"⏳ Días restantes: {dias}")

        if self.recordatorio:
            print(f"⏰ Recordatorio: {self.recordatorio.mensaje} ({self.recordatorio.fecha})")
        else:
            print("⏰ Recordatorio: (ninguno)")
