from datetime import date
from langchain_core.tools import tool

from ..database.book_service import book_service
from ..database.models import BookCreate, BookUpdate


@tool
def create_book(
    title: str, author: str = None, status: str = None, description: str = None
) -> str:
    """Crea un nuevo libro en la base de datos.

    Args:
        title: Título del libro (requerido)
        author: Autor del libro (opcional)
        status: Estado de lectura como 'reading', 'completed', 'pending' (opcional)
        description: Descripción del libro (opcional)

    Returns:
        Mensaje de confirmación con los detalles del libro creado
    """
    try:
        print("Desde la tool de create")
        book_data = BookCreate(
            title=title,
            author=author,
            status=status,
            type="test",
            description=description,
            is_physically=True,
            finished=date.fromisoformat("2025-12-12"),
        )
        book = book_service.create_book(book_data)
        # return f"Libro '{title}' creado exitosamente con ID {book.id}"
        return f"Libro '{title}' creado exitosamente "
    except Exception as e:
        return f"Error al crear el libro: {str(e)}"


@tool
def get_book(book_id: int) -> str:
    """Obtiene información detallada de un libro por su ID.

    Args:
        book_id: ID único del libro

    Returns:
        Información completa del libro o mensaje de error si no existe
    """
    try:
        book = book_service.get_book(book_id)
        if not book:
            return f"No se encontró ningún libro con ID {book_id}"

        return f"""Libro encontrado:
- ID: {book.id}
- Título: {book.title}
- Autor: {book.author or "No especificado"}
- Estado: {book.status or "No especificado"}
- Tipo: {book.type or "No especificado"}
- Descripción: {book.description or "Sin descripción"}
- Es físico: {"Sí" if book.is_physically else "No"}
- Fecha de finalización: {book.finished or "No finalizado"}
"""
    except Exception as e:
        return f"Error al obtener el libro: {str(e)}"


@tool
def update_book(
    book_id: int,
    title: str = None,
    author: str = None,
    status: str = None,
    description: str = None,
) -> str:
    """Actualiza la información de un libro existente.

    Args:
        book_id: ID del libro a actualizar (requerido)
        title: Nuevo título del libro (opcional)
        author: Nuevo autor del libro (opcional)
        status: Nuevo estado de lectura (opcional)
        description: Nueva descripción (opcional)

    Returns:
        Mensaje de confirmación con los datos actualizados
    """
    try:
        book_data = BookUpdate(
            title=title, author=author, status=status, description=description
        )
        book = book_service.update_book(book_id, book_data)
        if not book:
            return f"No se encontró ningún libro con ID {book_id}"

        return f"Libro '{book.title}' (ID: {book_id}) actualizado correctamente"
    except Exception as e:
        return f"Error al actualizar el libro: {str(e)}"


@tool
def delete_book(book_id: int) -> str:
    """Elimina un libro de la base de datos.

    Args:
        book_id: ID del libro a eliminar

    Returns:
        Mensaje de confirmación o error
    """
    try:
        deleted = book_service.delete_book(book_id)
        if deleted:
            return f"Libro con ID {book_id} eliminado exitosamente"
        else:
            return f"No se encontró ningún libro con ID {book_id}"
    except Exception as e:
        return f"Error al eliminar el libro: {str(e)}"


@tool
def list_books(status: str = None, author: str = None) -> str:
    """Lista todos los libros de la base de datos con filtros opcionales.

    Args:
        status: Filtrar por estado de lectura (opcional)
        author: Filtrar por autor (opcional)

    Returns:
        Lista formateada de libros encontrados
    """
    try:
        books = book_service.list_books(status=status, author=author)
        if not books:
            filters = []
            if status:
                filters.append(f"status='{status}'")
            if author:
                filters.append(f"author='{author}'")
            filter_str = " con filtros: " + ", ".join(filters) if filters else ""
            return f"No se encontraron libros{filter_str}"

        result = f"Encontrados {len(books)} libro(s):\n\n"
        for book in books:
            result += f"[{book.id}] {book.title}\n"
            result += f"    Autor: {book.author or 'No especificado'}\n"
            result += f"    Estado: {book.status or 'No especificado'}\n"
            if book.description:
                result += f"    Descripción: {book.description[:100]}...\n"
            result += "\n"

        return result
    except Exception as e:
        return f"Error al listar libros: {str(e)}"


# Lista de todas las tools disponibles para exportar
book_tools = [create_book, get_book, update_book, delete_book, list_books]
