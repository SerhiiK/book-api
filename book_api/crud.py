from sqlalchemy.orm import Session
from book_api.models import Books
from book_api.schemas import Book


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Books).offset(skip).limit(limit).all()


def get_books_by_id(db: Session, book_id: int):
    return db.query(Books).filter(Books.id == book_id).first()


def create_book_db(db: Session, book: Book):
    new_book = Books(title=book.title, author=book.author, pages=book.pages)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def edit_the_book(db: Session, book_id: int, book_data: dict):
    book_to_edit = db.query(Books).filter(Books.id == book_id).first()
    if not book_to_edit:
        raise ValueError(f"Book with id {book_id} not found")

    for key, value in book_data.items():
        if hasattr(book_to_edit, key):
            setattr(book_to_edit, key, value)
    db.commit()
    db.refresh(book_to_edit)
    return book_to_edit


def delete_book_from_db(db: Session, book_id: int) -> None:
    book_to_delete = db.query(Books).filter(Books.id == book_id).first()

    if not book_to_delete:
        raise ValueError(f"Book with id {book_id} not exist")

    db.delete(book_to_delete)
    db.commit()
