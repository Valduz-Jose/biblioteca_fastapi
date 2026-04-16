from sqlalchemy.orm import Session
from models.libro import Libro


# ---------------------------------------------
# SERVICIO: LISTAR LIBROS
# ---------------------------------------------
def listar_libros(db: Session):
    """
    Obtiene todos los libros de la base de datos.

    Parámetros:
        db (Session): sesión activa de SQLAlchemy

    Retorna:
        Lista de objetos Libro
    """
    return db.query(Libro).all()