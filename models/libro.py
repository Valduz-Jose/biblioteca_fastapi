from sqlalchemy import Column, Integer, String
from database import Base

# Definición del modelo Libro
class Libro(Base):
    """
    Esta clase representa la tabla 'libros' en la base de datos.
    Cada atributo de la clase corresponde a una columna.
    """

    __tablename__ = "libros"  # Nombre de la tabla en MySQL

    # Clave primaria autoincremental
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Título del libro (obligatorio)
    titulo = Column(String(255), nullable=False)

    # Autor del libro (obligatorio)
    autor = Column(String(255), nullable=False)

    # Rating del libro (obligatorio, valores esperados entre 1 y 5)
    rating = Column(Integer, nullable=False)