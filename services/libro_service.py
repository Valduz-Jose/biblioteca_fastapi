from sqlalchemy.orm import Session
from models.libro import Libro
from schemas import LibroCreate, LibroUpdate


# ---------------------------------------------
# SERVICIO: LISTAR LIBROS
# ---------------------------------------------
def listar_libros(db: Session):
    return db.query(Libro).all()


# ---------------------------------------------
# SERVICIO: CREAR LIBRO
# ---------------------------------------------
def crear_libro(db: Session, datos: LibroCreate):
    nuevo_libro = Libro(
        titulo=datos.titulo,
        autor=datos.autor,
        rating=datos.rating
    )

    db.add(nuevo_libro)
    db.commit()
    db.refresh(nuevo_libro)

    return nuevo_libro


# ---------------------------------------------
# SERVICIO: OBTENER LIBRO POR ID
# ---------------------------------------------
def obtener_libro_por_id(db: Session, id: int):
    return db.query(Libro).filter(Libro.id == id).first()


# ---------------------------------------------
# SERVICIO: ACTUALIZAR LIBRO
# ---------------------------------------------
def actualizar_libro(db: Session, id: int, datos: LibroUpdate):
    """
    Actualiza un libro existente.
    Permite actualización parcial (solo campos enviados).
    """

    libro = db.query(Libro).filter(Libro.id == id).first()

    if not libro:
        return None

    # Actualizar solo campos enviados (no None)
    if datos.titulo is not None:
        libro.titulo = datos.titulo

    if datos.autor is not None:
        libro.autor = datos.autor

    if datos.rating is not None:
        libro.rating = datos.rating

    db.commit()
    db.refresh(libro)

    return libro