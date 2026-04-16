from sqlalchemy.orm import Session
from models.libro import Libro
from schemas import LibroCreate


# ---------------------------------------------
# SERVICIO: LISTAR LIBROS
# ---------------------------------------------
def listar_libros(db: Session):
    """
    Obtiene todos los libros de la base de datos.
    """
    return db.query(Libro).all()


# ---------------------------------------------
# SERVICIO: CREAR LIBRO
# ---------------------------------------------
def crear_libro(db: Session, datos: LibroCreate):
    """
    Crea un nuevo libro en la base de datos.

    Parámetros:
        db: sesión de base de datos
        datos: información validada del libro (Pydantic)

    Retorna:
        Libro creado
    """

    nuevo_libro = Libro(
        titulo=datos.titulo,
        autor=datos.autor,
        rating=datos.rating
    )

    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)

    return nuevo_libro