from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(min_length=4)
    author: str = Field(min_length=5)
    pages: int = Field(gt=0, lt=5000)


class BookUpdate(BaseModel):
    title: str | None = Field(
        None, min_length=4, max_length=100
    )  # Min 4, max 100 characters
    author: str | None = Field(
        None, min_length=5, max_length=50
    )  # Min 5, max 50 characters
    pages: int | None = Field(None, gt=0, lt=5000)
