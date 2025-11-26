
from .sistema_amistapp import Sistema_amistapp
from .amigo import Amigo
from interes import Interes
from .evento import Evento
from .cumpleanios import Cumpleanios
from .recordatorio import Recordatorio


def mostrar_menu():
    print("""
===============================
 🎀 MENÚ PRINCIPAL AMISTAPP 🎀
===============================

1️⃣  Agregar amigo
2️⃣  Agregar actividad (evento o cumpleaños)
3️⃣  Agregar interés
4️⃣  Eliminar actividad
5️⃣  Mostrar todo
6️⃣  Salir
    """)


def agregar_amigo(sistema: Sistema_amistapp):
    nombre = input("👤 Nombre: ")
    apellido = input("👤 Apellido: ")
    apodo = input("💬 Apodo: ")
    genero = input("🚻 Género: ")
    amigo = Amigo(nombre, apellido, apodo, genero)
    sistema.agregar_amigo(amigo)


def agregar_actividad(sistema):
    tipo = input("¿Qué tipo de actividad deseas agregar? (evento/cumpleanios): ").strip().lower()

    if tipo == "evento":
        titulo = input("📌 Título del evento: ")
        fecha = input("📅 Fecha (AAAA-MM-DD): ")
        descripcion = input("📝 Descripción: ")
        lugar = input("📍 Lugar: ")
        duracion = float(input("⏱️ Duración (en horas): "))
        importancia = int(input("🔥 Nivel de importancia (1-10): "))
        estado = input("📌 Estado del evento: ")

        mensaje_rec = input("💌 Mensaje del recordatorio: ")
        fecha_rec = input("⏰ Fecha del recordatorio (AAAA-MM-DD): ")
      
        recordatorio = Recordatorio(mensaje_rec, fecha_rec)

        evento = Evento(titulo, fecha, descripcion, recordatorio, lugar, duracion, importancia, estado)
        sistema.agregar_actividad(evento)

    elif tipo == "cumpleanios":
        nombre = input("🎂 Nombre del cumpleañero: ")
        fecha = input("📅 Fecha de cumpleaños (AAAA-MM-DD): ")
        descripcion = input("📝 Descripción: ")
        mensaje_rec = input("💌 Mensaje del recordatorio: ")
        fecha_rec = input("⏰ Fecha del recordatorio (AAAA-MM-DD): ")
        mensaje_felicitacion = input("🎉 Mensaje de felicitación: ")

        recordatorio = Recordatorio(mensaje_rec, fecha_rec)

        cumple = Cumpleanios(nombre, fecha, descripcion, recordatorio, mensaje_felicitacion)
        sistema.agregar_actividad(cumple)

    else:
        print("⚠️ Tipo de actividad no válido.")


def agregar_interes(sistema: Sistema_amistapp):
    nombre = input("🎯 Nombre del interés: ")
    descripcion = input("📝 Descripción: ")

    Interes.mostrar_categorias_disponibles()
    categoria = input("🏷️ Categoría: ")

    nivel_frecuencia = int(input("🔁 Nivel de frecuencia (1-10): "))
    interes = Interes(nombre, descripcion, categoria, nivel_frecuencia)

    sistema.agregar_interes(interes)




if __name__ == "__main__":

    sistema = Sistema_amistapp()

    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            agregar_amigo(sistema)
        elif opcion == "2":
            agregar_actividad(sistema)
        elif opcion == "3":
            agregar_interes(sistema)
        elif opcion == "4":
            titulo = input("🗑️ Escribe el título de la actividad a eliminar: ")
            sistema.eliminar_actividad(titulo)
        elif opcion == "5":
            sistema.mostrar_todo()
        elif opcion == "6":
            print("👋 ¡Gracias por usar AmistApp! 💖")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")
