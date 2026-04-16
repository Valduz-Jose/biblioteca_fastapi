from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


# -------------------------
# BASE: campos comunes
# -------------------------
class LibroBase(BaseModel):
    """
    Campos base compartidos entre creación y actualización.
    """

    titulo: str = Field(..., min_length=1, description="Título del libro (obligatorio)")
    autor: str = Field(..., min_length=1, description="Autor del libro (obligatorio)")
    rating: int = Field(..., ge=1, le=5, description="Rating entre 1 y 5")


# -------------------------
# CREACIÓN
# -------------------------
class LibroCreate(LibroBase):
    """
    Esquema para crear un libro.
    Hereda validaciones de LibroBase.
    """
    pass


# -------------------------
# ACTUALIZACIÓN
# -------------------------
class LibroUpdate(BaseModel):
    """
    Esquema para actualizar libros.
    Todos los campos son opcionales para permitir actualización parcial.
    """

    titulo: Optional[str] = Field(None, min_length=1)
    autor: Optional[str] = Field(None, min_length=1)
    rating: Optional[int] = Field(None, ge=1, le=5)


# -------------------------
# RESPUESTA (READ)
# -------------------------
class LibroRead(LibroBase):
    """
    Esquema de salida hacia la API.
    Incluye el ID generado por la base de datos.
    """

    id: int

    # Permite mapear desde SQLAlchemy a Pydantic
    model_config = ConfigDict(from_attributes=True)