from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from services.libro_service import (
    listar_libros,
    crear_libro,
    obtener_libro_por_id,
    actualizar_libro
)
from schemas import LibroRead, LibroCreate, LibroUpdate

# Router principal para libros
router = APIRouter(
    prefix="/api/libros",
    tags=["Libros"]
)


# ---------------------------------------------
# LISTAR LIBROS
# ---------------------------------------------
@router.get("/", response_model=List[LibroRead])
def get_libros(db: Session = Depends(get_db)):
    return listar_libros(db)


# ---------------------------------------------
# CREAR LIBRO
# ---------------------------------------------
@router.post("/", response_model=LibroRead, status_code=status.HTTP_201_CREATED)
def create_libro(libro: LibroCreate, db: Session = Depends(get_db)):
    return crear_libro(db, libro)


# ---------------------------------------------
# OBTENER LIBRO POR ID
# ---------------------------------------------
@router.get("/{id}", response_model=LibroRead)
def get_libro_by_id(id: int, db: Session = Depends(get_db)):
    libro = obtener_libro_por_id(db, id)

    if not libro:
        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    return libro


# ---------------------------------------------
# ACTUALIZAR LIBRO
# ---------------------------------------------
@router.put("/{id}", response_model=LibroRead)
def update_libro(id: int, datos: LibroUpdate, db: Session = Depends(get_db)):
    """
    Actualiza un libro existente.
    """

    libro_actualizado = actualizar_libro(db, id, datos)

    if not libro_actualizado:
        raise HTTPException(
            status_code=404,
            detail="Libro no encontrado"
        )

    return libro_actualizado