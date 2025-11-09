from sistema_amistapp import SistemaAmistapp
from amigo import Amigo
from interes import Interes
from evento import Evento
from cumpleanios import Cumpleaños
from recordatorio import Recordatorio

def mostrar_menu():
    print("""
          🎀 MENÚ PRINCIPAL AMISTAPP 🎀
1️⃣  Agregar amigo
2️⃣  Agregar evento
3️⃣  Agregar cumpleaños
4️⃣  Mostrar todo
5️⃣  Salir
          """)
def main():
    sistema = SistemaAmistapp()
    
    while True:
        mostrar_menu()
        opcion = input("➡️ Selecciona una opción: ")
        if opcion == "1":
            agregar_amigo(sistema)
        elif opcion == "2":
            agregar_evento(sistema)
        elif opcion == "3":
            agregar_cumpleanios(sistema)
        elif opcion == "4":
            sistema.mostrar_todo()
        elif opcion == "5":
            print("👋 ¡Gracias por usar AmistApp!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")
            
def agregar_amigo(sistema):
    print("\n🫂 --- Agregar nuevo amigo ---")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    apodo = input("Apodo: ")
    genero = input("Género: ")

    nuevo_amigo = Amigo(nombre, apellido, apodo, genero)

    while True:
        agregar = input("¿Deseas agregar un interés a este amigo? (s/n): ").lower()
        if agregar == "s":
            Interes.mostrar_categorias_disponibles()
            nombre_i = input("Nombre del interés: ")
            descripcion = input("Descripción: ")
            categoria = input("Categoría: ")
            nivel = int(input("Nivel de frecuencia (1-10): "))
            interes = Interes(nombre_i, descripcion, categoria, nivel)
            nuevo_amigo.agregar_interes(interes)
        else:
            break

    sistema.amigos.append(nuevo_amigo)
    print(f"✅ Amigo '{nombre}' agregado con éxito.")

    