from fastapi import FastAPI
from api.libros import router as libros_router

# Creamos una instancia de FastAPI
# Esta será el núcleo de nuestra aplicación
app = FastAPI()


# Endpoint de prueba
@app.get("/")
def read_root():
    """
    Endpoint básico para verificar que la API está funcionando.

    Cuando accedemos a http://localhost:8000/
    devuelve un mensaje simple en formato JSON.
    """
    return {"mensaje": "¡API de Biblioteca funcionando correctamente!"}

# Registrar rutas de libros
app.include_router(libros_router)