import os
from alembic import command
from alembic.config import Config
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Cargar variables de entorno
load_dotenv()

# Configuración de Alembic
alembic_cfg = Config("alembic.ini")

# URL de conexión
DB_URL = "mysql+pymysql://root:admin@localhost:3306/biblioteca_db"


def limpiar_alembic_version_si_es_necesario():
    """
    Elimina la tabla alembic_version si existe pero está corrupta o desincronizada.
    """
    engine = create_engine(DB_URL)
    with engine.connect() as conn:
        try:
            conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
            print("🧹 Tabla alembic_version limpiada (si existía)")
        except Exception as e:
            print("⚠️ No se pudo limpiar alembic_version:", e)


def ejecutar_migraciones():
    """
    Genera una migración automática y la aplica.
    """
    print("📦 Generando migración...")
    command.revision(alembic_cfg, message="crear tabla libros", autogenerate=True)

    print("⬆️ Aplicando migración...")
    command.upgrade(alembic_cfg, "head")

    print("✅ Migraciones aplicadas correctamente")


if __name__ == "__main__":
    limpiar_alembic_version_si_es_necesario()
    ejecutar_migraciones()