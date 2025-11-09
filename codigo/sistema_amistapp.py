from amigo import Amigo 
from evento import Evento 

class SistemaAmistapp:
    def __init__(self):
        self.eventos = []
        self.amigos = []
        
    def agregar_evento(self, evento: Evento):
        self.eventos. append(evento)
        print(f"✅Evento '{evento.titulo}' se agrego correctamente 😁.")
        
    def eliminar_evento(self, titulo: str):
        for evento in self.eventos:
            if evento.titulo == titulo:
                self.eventos.remove(evento)
                print(f"✖️Evento {titulo} eliminado.")
                return
        print(f"⚠️ no se ha encontrado ningun evento con ese titulo😕.")
    def buscar_amigo(self, nombre: str):
        for amigo in self.amigos:
            if amigo.nombre == nombre:
                print(f"🫂 Amigo encontrado: {amigo.nombre}")
                return amigo
        print(f"⚠️ no se ha encontrado ningun amigo con el nombre{nombre}.")
        return None     
        
    def mostrar_todo(self):
        print("\n📚  LISTA DE AMIGOS ")
        if self.amigos:
            for amigo in self.amigos:
                print(f"⭐{amigo.nombre}-{amigo.apodo}")
        else:
            print("no hay amigos registrados.")
        print("\n🎉 LISTA DE EVENTOS ")
        if self.eventos:
            for evento in self.eventos:
                print(f"-{evento.titulo} ({evento.fecha}) ({evento.duracion}) ({evento.importancia}) ({evento.estado})")
        else:
            print("No hay eventos registrados.")