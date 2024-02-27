from pydantic import BaseModel


class Thumbnail(BaseModel):

    thumbnail: str
    small_thumbnail: str


class Book(BaseModel):

    title: str
    authors: list[str]
    page_count: int | None
    language: str
    published_date: str
    google_id: str
    google_link: str | None
    thumbnail: Thumbnail
