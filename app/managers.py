from typing import Any, Self
from clients.google_books.client import GoogleBooksClient
from clients.google_books.schemas import GoogleBooksResponse 
from .schemas import Book, Thumbnail


class BookManager:

    client: GoogleBooksClient

    def __init__(self: Self, api_key: str, uri: str) -> None:
        self.client = GoogleBooksClient(api_key, uri)
    
    def _parse_book_data(self: Self, volumes: list[GoogleBooksResponse]) -> list[Book]:
        books = []
        for volume in volumes.items:
            thumbnail = None
            if volume.volume_info.image_links:
                thumbnail = Thumbnail.parse_obj(volume.volume_info.image_links.__dict__)
            books.append(
                Book(
                    title=volume.volume_info.title,
                    authors=volume.volume_info.authors,
                    page_count=volume.volume_info.page_count,
                    language=volume.volume_info.language,
                    published_date=volume.volume_info.published_date,
                    thumbnail=thumbnail,
                    google_id=volume.id,
                    google_link=volume.self_link
                )
            )
        return books
    
    async def get_books(self: Self, q: str) -> list[Book]:
        volumes = await self.client.get_books_from_api(q)
        return self._parse_book_data(volumes)

