from typing import Any, Self
from httpx import AsyncClient
from .schemas import GoogleBooksResponse



class GoogleBooksClient:

    api_key: str
    uri: str

    def __init__(self: Self, api_key: str, uri: str) -> None:
        self.api_key = api_key
        self.uri = uri

    async def get_books_from_api(self: Self, q: str) -> GoogleBooksResponse:
        async with AsyncClient() as client:
            response = await client.get(
                f"{self.uri}{q}&key={self.api_key}"
            )
        
        return GoogleBooksResponse.parse_obj(response.json())
