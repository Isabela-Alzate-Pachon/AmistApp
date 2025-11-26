from fastapi import FastAPI
import sys
from pathlib import Path

# Agregar la carpeta codigo al path
sys.path.append(str(Path(__file__).parent.parent))

# Importar los routers
from router import amigo_router
from router import interes_router
from router import actividad_router
from router import evento_router
from router import cumpleanios_router
from router import recordatorio_router

# Crear la aplicación
app = FastAPI(title="AmistApp API", version="1.0")

# Conectar los routers
app.include_router(amigo_router.router, prefix="/amigos", tags=["Amigos"])
app.include_router(interes_router.router, prefix="/intereses", tags=["Intereses"])
app.include_router(actividad_router.router, prefix="/actividades", tags=["Actividades"])
app.include_router(evento_router.router, prefix="/eventos", tags=["Eventos"])
app.include_router(cumpleanios_router.router, prefix="/cumpleanios", tags=["Cumpleaños"])
app.include_router(recordatorio_router.router, prefix="/recordatorios", tags=["Recordatorios"])

# Página principal
@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a AmistApp API",
        "documentacion": "http://localhost:8000/docs"
    }

# Para ejecutar: python main.py
if __name__ == "__main__":
    import uvicorn
    print("🚀 Iniciando AmistApp API...")
    print("📚 Ve la documentación en: http://localhost:8000/docs")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
