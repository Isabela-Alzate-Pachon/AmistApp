class Interes: 
    CATEGORIAS_VALIDAS = (
        "Deporte",
        "Arte",
        "Tecnología",
        "Música",
        "Lectura",
        "Viajes",
        "Cocina",
        "Videojuegos",
        "Cine",
        "Otros"
    )
    
    def __init__(self, nombre: str, descripcion: str, categoria: str,nivel_frecuencia: int): 
        self.nombre = nombre
        self.descripcion = descripcion 
        self.nivel_frecuencia = nivel_frecuencia 
        
        if categoria not in Interes.CATEGORIAS_VALIDAS:
            print(F"⚠️ Categoría '{categoria}' no válida. Se asignará 'Otros'.")
            self.categoria = "Otros"
        else:
            self.categoria = categoria
    
    def mostrar_info(self):
        print(f"\n🎯 Interés: {self.nombre}")
        print(f"📝 Descripción: {self.descripcion}") 
        print(f"🏷️ Categoría: {self.categoria}")
        print(f"🔁 Nivel de frecuencia: {self.nivel_frecuencia}/10")
    
    def agregar_interes (self,subinteres: str):
        self.descripcion += f", también le gusta {subinteres}"
        print(f"➕ Se agregó un nuevo subinterés: {subinteres}")
    @staticmethod    
    def mostrar_categorias_disponibles():
         print("\n📚 Categorías disponibles:")
         for categoria in Interes.CATEGORIAS_VALIDAS:
            print(f" - {categoria}")