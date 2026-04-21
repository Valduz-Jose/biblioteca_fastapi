from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.libros import router as libros_router
from database import Base, engine

# ---------------------------------------------
# INSTANCIA PRINCIPAL DE FASTAPI
# ---------------------------------------------
app = FastAPI(
    title="Biblioteca Personal API",
    description="API REST para gestión de libros",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)

# ---------------------------------------------
# CONFIGURACIÓN CORS
# ---------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # "http://localhost:4200",  # Angular
        # "http://localhost:5173"   # React (Vite)
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------
# ENDPOINT DE PRUEBA
# ---------------------------------------------
@app.get("/")
def root():
    return {"message": "API Biblioteca funcionando 🚀"}

# ---------------------------------------------
# INCLUIR ROUTERS
# ---------------------------------------------
app.include_router(libros_router)