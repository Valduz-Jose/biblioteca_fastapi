import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construir URL de conexión
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear engine (conexión base)
engine = create_engine(
    DATABASE_URL,
    echo=True  # Muestra logs SQL en consola (útil para desarrollo)
)

# Crear sesión
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos
Base = declarative_base()


# Dependencia para FastAPI
def get_db():
    """
    Genera una sesión de base de datos por cada request.
    Se asegura de cerrarla correctamente al finalizar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Prueba de conexión
if __name__ == "__main__":
    try:
        with engine.connect() as connection:
            print("✅ Conexión a la base de datos exitosa")
    except Exception as e:
        print("❌ Error al conectar a la base de datos:")
        print(e)