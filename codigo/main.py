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

def agregar_amigo(sistema: SistemaAmistapp):
    nombre = input("👤 Nombre: ")
    apellido = input("👤 Apellido: ")
    apodo = input("💬 Apodo: ")
    genero = input("🚻 Género: ")

    amigo = Amigo(nombre, apellido, apodo, genero)
    sistema.agregar_amigo(amigo)
    print("✅ Amigo agregado exitosamente.")


def agregar_evento(sistema: SistemaAmistapp):
    titulo = input("📌 Título del evento: ")
    fecha = input("📅 Fecha (AAAA-MM-DD): ")
    descripcion = input("📝 Descripción: ")
    lugar = input("📍 Lugar: ")
    duracion = float(input("⏱️ Duración (en horas): "))
    nivel_importancia = int(input("🔥 Nivel de importancia (1-10): "))
    estado = input("📌 Estado del evento: ")

    mensaje_recordatorio = input("💌 Mensaje del recordatorio: ")
    fecha_recordatorio = input("⏰ Fecha del recordatorio (AAAA-MM-DD): ")
    recordatorio = Recordatorio(mensaje_recordatorio, fecha_recordatorio)

    evento = Evento(fecha, recordatorio, lugar, duracion, nivel_importancia, estado)
    sistema.agregar_evento(evento)
    print("✅ Evento agregado exitosamente.")


def agregar_cumpleaños(sistema: SistemaAmistapp):
    titulo = input("🎂 Nombre del cumpleañero: ")
    fecha = input("📅 Fecha de cumpleaños (AAAA-MM-DD): ")
    descripcion = input("📝 Descripción: ")
    mensaje_recordatorio = input("💌 Mensaje del recordatorio: ")
    fecha_recordatorio = input("⏰ Fecha del recordatorio (AAAA-MM-DD): ")
    mensaje_felicitaciones = input("🎉 Mensaje de felicitación: ")

    recordatorio = Recordatorio(mensaje_recordatorio, fecha_recordatorio)
    cumple = Cumpleaños(titulo, fecha, descripcion, recordatorio, mensaje_felicitaciones)
    sistema.agregar_cumpleaños(cumple)
    print("✅ Cumpleaños agregado exitosamente.")


# ------------------- BLOQUE PRINCIPAL -------------------

if __name__ == "__main__":
    sistema = SistemaAmistapp()

    while True:
        mostrar_menu()
        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            agregar_amigo(sistema)
        elif opcion == "2":
            agregar_evento(sistema)
        elif opcion == "3":
            agregar_cumpleaños(sistema)
        elif opcion == "4":
            sistema.mostrar_todo()
        elif opcion == "5":
            print("👋 ¡Gracias por usar AmistApp! Hasta pronto.")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")
