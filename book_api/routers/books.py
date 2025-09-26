from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from book_api.database import get_db
from book_api.schemas import Book, BookUpdate
from ..crud import (
    delete_book_from_db,
    get_books,
    get_books_by_id,
    create_book_db,
    edit_the_book,
)


book = APIRouter()


@book.get("/books/", summary="Get all books")
async def read_books(db: Session = Depends(get_db)):
    books_list = get_books(db)
    return books_list


@book.get(
    "/books/{book_id}",
    summary="Get book Title by ID",
    description="Return book by book_id.",
)
async def get_books_id(book_id: int, db: Session = Depends(get_db)):
    book = get_books_by_id(db, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found",
        )
    return book


@book.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete book by ID",
)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    try:
        deleted_book = delete_book_from_db(db, book_id)
        return {"message": "Book was deleted", "book": deleted_book}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@book.post("/books/", status_code=status.HTTP_201_CREATED, summary="Create book")
async def create_book(book: Book, db: Session = Depends(get_db)):
    created_book = create_book_db(db, book)
    return created_book


@book.put("/books/{book_id}", summary="Edit book by ID")
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    try:
        updated_book = edit_the_book(db, book_id, book.model_dump(exclude_unset=True))
        return {"message": "Book was updated", "book": updated_book}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
