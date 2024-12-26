from fastapi import FastAPI
from .routers import books


app = FastAPI(title="Book API app", version="0.0.1")


app.include_router(books.book, prefix="/v1", tags=["books"])
