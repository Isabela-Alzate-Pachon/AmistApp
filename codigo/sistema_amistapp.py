from .amigo import Amigo
from .evento import Evento
from .cumpleanios import Cumpleanios
from .interes import Interes
from .actividad import Actividad



class Sistema_amistapp:
    def __init__(self):
        self.amigos = []
        self.intereses = []
        self.actividades = []
        self.cumpleanios = []  

    
    # AMIGOS
    
    def agregar_amigo(self, amigo: Amigo):
        self.amigos.append(amigo)
        print(f"✅ Amigo '{amigo.nombre}' agregado correctamente 🫶.")

    def buscar_amigo(self, nombre: str):
        for amigo in self.amigos:
            if amigo.nombre.lower() == nombre.lower():
                print(f"🫂 Amigo encontrado: {amigo.nombre}")
                return amigo
        print(f"⚠️ No se ha encontrado ningún amigo con el nombre '{nombre}'.")
        return None

   
    # INTERESES
   
    def agregar_interes(self, interes: Interes):
        self.intereses.append(interes)
        print(f"🎯 Interés '{interes.nombre}' agregado correctamente 🧠.")

    
    # ACTIVIDADES
    
    def agregar_actividad(self, actividad: Actividad):
        self.actividades.append(actividad)
        print(f"✅ Actividad '{actividad.__class__.__name__}' agregada correctamente 😁.")

    def eliminar_actividad(self, titulo: str):
        for actividad in self.actividades:
            if hasattr(actividad, "titulo") and actividad.titulo == titulo:
                self.actividades.remove(actividad)
                print(f"✖️ Actividad '{titulo}' eliminada correctamente.")
                return
        print(f"⚠️ No se encontró ninguna actividad con el título '{titulo}'.")

    # CUMPLEAÑOS
   
    def agregar_cumpleanios(self, cumple: Cumpleanios):
        self.cumpleanios.append(cumple)
        print(f"🎂 Cumpleaños de '{cumple.titulo}' agregado correctamente 🎉.")

    # MOSTRAR TODO
    
    def mostrar_todo(self):
        print("\n📚 LISTA DE AMIGOS")
        if self.amigos:
            for amigo in self.amigos:
                print(f"⭐ {amigo.nombre} - {amigo.apodo}")
        else:
            print("No hay amigos registrados.")

        print("\n🎉 LISTA DE ACTIVIDADES")
        if self.actividades:
            for actividad in self.actividades:
                actividad.mostrar_actividad()
        else:
            print("No hay actividades registradas.")

        print("\n🎂 LISTA DE CUMPLEAÑOS")
        if self.cumpleanios:
            for c in self.cumpleanios:
                c.mostrar_actividad()
        else:
            print("No hay cumpleaños registrados.")

        print("\n💖 LISTA DE INTERESES")
        if self.intereses:
            for interes in self.intereses:
                print(f"🎯 {interes.nombre} - {interes.categoria} ({interes.nivel_frecuencia}/10)")
        else:
            print("No hay intereses registrados.")
