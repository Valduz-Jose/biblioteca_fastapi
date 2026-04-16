from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from services.libro_service import listar_libros
from schemas import LibroRead

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

    libros = listar_libros(db)

    return libros