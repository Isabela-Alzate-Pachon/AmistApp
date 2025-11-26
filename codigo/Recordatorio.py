


class Recordatorio:
    def __init__(self, mensaje: str, fecha: str):
        self.mensaje = mensaje
        self.fecha = fecha
        
    def mostrar_recordatorio(self):
        print(f"📅 Recordatorio: {self.mensaje} - Fecha: {self.fecha}")