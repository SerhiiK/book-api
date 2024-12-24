import pytest
from fastapi.testclient import TestClient
from book_api.routers.books import book 

client = TestClient(book)

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
