from typing import Optional, Any
from pydantic import BaseModel, Field


class Thumbnail(BaseModel):

    thumbnail: str
    small_thumbnail: str = Field(alias="smallThumbnail")


class IndustryIdentifiers(BaseModel):

    type: str
    identifier: str


class ReadingModes(BaseModel):

    text: bool
    image: bool


class PanelizationSummary(BaseModel):

    contains_epub_bubbles: bool = Field(alias="containsEpubBubbles")
    contains_image_bubbles: bool = Field(alias="containsImageBubbles")


class VolumeInfo(BaseModel):

    title: str
    subtitle: str = None
    authors: list[str]
    publisher: str = None
    published_date: str = Field(alias="publishedDate", default=None)
    description: str = None
    industry_identifiers: list[IndustryIdentifiers] = Field(alias="industryIdentifiers")
    reading_modes: ReadingModes = Field(alias="readingModes")
    print_type: str = Field(alias="printType")
    categories: list[str] = None
    maturity_rating: str = Field(alias="maturityRating")
    allow_anon_logging: bool = Field(alias="allowAnonLogging")
    content_version: str = Field(alias="contentVersion")
    panelization_summary: PanelizationSummary = Field(
        alias="panelizationSummary", default=None
    )
    image_links: Thumbnail = Field(alias="imageLinks", default=None)
    language: str
    preview_link: str = Field(alias="previewLink")
    info_link: str = Field(alias="infoLink", default=None)
    canonical_volume_link: str = Field(alias="canonicalVolumeLink")
    page_count: int = Field(alias="pageCount", default=None)


class Epub(BaseModel):

    is_available: bool = Field(alias="isAvailable")
    acs_token_link: str = Field(alias="acsTokenLink", default=None)


class Pdf(BaseModel):

    is_available: bool = Field(alias="isAvailable")


class Price(BaseModel):

    amount: float = None
    amount_in_micros: int = Field(alias="amountInMicros", default=None)
    currency_code: str = Field(alias="currencyCode")


class ListPrice(Price):
    ...


class RetailPrice(Price):
    ...


class Offer(BaseModel):

    finsky_offer_type: Optional[int] = Field(alias="finskyOfferType")
    list_price: ListPrice = Field(alias="listPrice", default=None)
    retail_price: RetailPrice = Field(alias="retailPrice", default=None)
    giftable: bool = None


class SaleInfo(BaseModel):

    country: str
    saleability: str
    is_ebook: bool = Field(alias="isEbook")
    list_price: ListPrice = Field(alias="listPrice", default=None)
    retail_price: RetailPrice = Field(alias="retailPrice", default=None)
    buy_link: str = None
    offers: list[Offer] = Field(default=None)


class AccessInfo(BaseModel):
    country: str
    viewability: str
    embeddable: bool
    public_domain: bool = Field(alias="publicDomain")
    text_to_speech_permission: str = Field(alias="textToSpeechPermission")
    epub: Epub
    pdf: Pdf
    web_reader_link: str = Field(alias="webReaderLink")
    access_view_status: str = Field(alias="accessViewStatus")
    quote_sharing_allowed: bool = Field(alias="quoteSharingAllowed")


class SearchInfo(BaseModel):

    text_snippet: str = Field(alias="textSnippet")


class Volume(BaseModel):

    kind: str
    id: str
    etag: str
    self_link: Any = None
    volume_info: VolumeInfo = Field(alias="volumeInfo")
    sale_info: SaleInfo = Field(alias="saleInfo")
    access_info: AccessInfo = Field(alias="accessInfo")
    search_info: SearchInfo = Field(alias="searchInfo", default=None)


class GoogleBooksResponse(BaseModel):

    kind: str
    total_items: int = Field(alias="totalItems")
    items: list[Volume]
