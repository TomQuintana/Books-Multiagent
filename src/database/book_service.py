from typing import List, Optional
from .models import Book, BookCreate, BookUpdate


class BookService:
    """Servicio para operaciones CRUD de libros"""

    def __init__(self):
        # TODO: Inicializar conexión a la base de datos
        pass

    def create_book(self, book_data: BookCreate) -> Book:
        """Crea un nuevo libro en la base de datos"""
        # TODO: Implementar lógica de creación en DB
        return "ok"

    def get_book(self, book_id: int) -> Optional[Book]:
        """Obtiene un libro por su ID"""
        # TODO: Implementar lógica de consulta en DB
        return "ok"

    def update_book(self, book_id: int, book_data: BookUpdate) -> Optional[Book]:
        """Actualiza un libro existente"""
        # TODO: Implementar lógica de actualización en DB
        return "ok"

    def delete_book(self, book_id: int) -> bool:
        """Elimina un libro por su ID"""
        # TODO: Implementar lógica de eliminación en DB
        return "ok"

    def list_books(self, status: str = None, author: str = None) -> List[Book]:
        """Lista libros con filtros opcionales"""
        # TODO: Implementar lógica de listado con filtros en DB
        return "ok"


# Instancia global del servicio
book_service = BookService()
