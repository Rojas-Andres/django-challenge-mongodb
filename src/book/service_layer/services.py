from src.book.domain.repository import AbstractBookUnitOfWork
from bson.decimal128 import Decimal128
from decimal import Decimal
from datetime import date


class CreateBlogService:
    def __init__(
        self,
        uow: AbstractBookUnitOfWork,
    ):
        self.uow = uow

    def create(
        self,
        title: str,
        author: str,
        published_date: date,
        genre: str,
        price: float,
    ) -> str:
        validate_exist = self.uow.book.validate_book_exist(
            title=title, author=author, published_date=published_date, genre=genre
        )
        if validate_exist:
            raise ValueError("Blog already exists")
        blog = self.uow.book.create(
            title=title,
            author=author,
            published_date=published_date,
            genre=genre,
            price=Decimal(price),
        )
        return blog