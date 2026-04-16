from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from services.libro_service import listar_libros, crear_libro
from schemas import LibroRead, LibroCreate

# Router principal para libros
router = APIRouter(
    prefix="/api/libros",
    tags=["Libros"]
)


# ---------------------------------------------
# ENDPOINT: LISTAR LIBROS
# ---------------------------------------------
@router.get("/", response_model=List[LibroRead])
def get_libros(db: Session = Depends(get_db)):
    """
    Devuelve todos los libros registrados en la base de datos.
    """
    return listar_libros(db)


# ---------------------------------------------
# ENDPOINT: CREAR LIBRO
# ---------------------------------------------
@router.post(
    "/",
    response_model=LibroRead,
    status_code=status.HTTP_201_CREATED
)
def create_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo libro en la base de datos.
    """
    return crear_libro(db, libro)