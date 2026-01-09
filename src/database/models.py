from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field


class Book(BaseModel):
    """Modelo de datos para un libro"""
    id: Optional[int] = Field(None, description="ID único del libro (autogenerado)")
    title: str = Field(..., description="Título del libro")
    author: Optional[str] = Field(None, description="Autor del libro")
    status: Optional[str] = Field(None, description="Estado de lectura (ej: 'reading', 'completed', 'pending')")
    type: Optional[str] = Field(None, description="Tipo de libro (ej: 'fiction', 'non-fiction', 'technical')")
    description: Optional[str] = Field(None, description="Descripción del libro")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación del registro")
    is_physically: Optional[bool] = Field(False, description="Indica si el libro es físico o digital")
    finished: Optional[date] = Field(None, description="Fecha en que se terminó de leer el libro")

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "title": "El Quijote",
                "author": "Miguel de Cervantes",
                "status": "completed",
                "type": "fiction",
                "description": "La historia de un hidalgo que pierde la razón",
                "is_physically": True,
                "finished": "2024-01-15"
            }
        }


class BookCreate(BaseModel):
    """Schema para crear un libro (sin ID)"""
    title: str = Field(..., min_length=1, description="Título del libro")
    author: Optional[str] = Field(None, description="Autor del libro")
    status: Optional[str] = Field(None, description="Estado de lectura")
    type: Optional[str] = Field(None, description="Tipo de libro")
    description: Optional[str] = Field(None, description="Descripción del libro")
    is_physically: Optional[bool] = Field(False, description="Si el libro es físico")
    finished: Optional[date] = Field(None, description="Fecha de finalización")


class BookUpdate(BaseModel):
    """Schema para actualizar un libro (todos los campos opcionales)"""
    title: Optional[str] = Field(None, min_length=1, description="Título del libro")
    author: Optional[str] = Field(None, description="Autor del libro")
    status: Optional[str] = Field(None, description="Estado de lectura")
    type: Optional[str] = Field(None, description="Tipo de libro")
    description: Optional[str] = Field(None, description="Descripción del libro")
    is_physically: Optional[bool] = Field(None, description="Si el libro es físico")
    finished: Optional[date] = Field(None, description="Fecha de finalización")
