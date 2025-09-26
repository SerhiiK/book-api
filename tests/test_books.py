import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from book_api.database import Base, get_db
from book_api.main import app
from book_api.models import Books


engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(autouse=True)
def prepare_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with TestingSessionLocal() as session:
        session.add_all(
            [
                Books(title="Clean Code", author="Robert C. Martin", pages=464),
                Books(
                    title="The Pragmatic Programmer",
                    author="Andy Hunt and Dave Thomas",
                    pages=352,
                ),
            ]
        )
        session.commit()
    yield
    Base.metadata.drop_all(bind=engine)


def test_get_books():
    response = client.get("/v1/books/")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 2
    titles = {book["title"] for book in payload}
    assert {"Clean Code", "The Pragmatic Programmer"} == titles


def test_get_book_by_id():
    response = client.get("/v1/books/1")
    assert response.status_code == 200
    payload = response.json()
    assert payload["title"] == "Clean Code"
    assert payload["author"] == "Robert C. Martin"


def test_create_book():
    new_book = {"title": "Refactoring", "author": "Martin Fowler", "pages": 431}
    response = client.post("/v1/books/", json=new_book)
    assert response.status_code == 201
    payload = response.json()
    assert payload["id"] == 3
    assert payload["title"] == new_book["title"]


def test_update_book():
    update_payload = {"title": "Clean Code Revised", "pages": 470}
    response = client.put("/v1/books/1", json=update_payload)
    assert response.status_code == 200
    payload = response.json()
    assert payload["message"] == "Book was updated"
    assert payload["book"]["title"] == "Clean Code Revised"
    assert payload["book"]["pages"] == 470


def test_delete_book():
    response = client.delete("/v1/books/1")
    assert response.status_code == 204
    assert response.content in (b"", b"null")

    get_response = client.get("/v1/books/1")
    assert get_response.status_code == 404
