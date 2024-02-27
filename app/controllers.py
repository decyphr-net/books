from typing import Annotated
from fastapi import APIRouter, Depends
from settings import Settings, get_settings
from .managers import BookManager
from .schemas import Book

router = APIRouter()


@router.get("/api/books", response_model=None)
async def get_books(
    q: str, settings: Annotated[Settings, Depends(get_settings)]
) -> list[Book]:
    response = await BookManager(
        settings.google_books_api_key, settings.google_books_uri
    ).get_books(q) 
    return response
