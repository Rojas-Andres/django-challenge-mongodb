from src.book.domain.repository import AbstractBookUnitOfWork
from bson.decimal128 import Decimal128
from decimal import Decimal
from datetime import date
from shared.tools import validate_object_id

# import Optional
from typing import Optional


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


class DeleteBlogService:
    def __init__(
        self,
        uow: AbstractBookUnitOfWork,
    ):
        self.uow = uow

    def delete(
        self,
        book_id: str,
    ) -> str:
        validate_object_id(id=book_id)
        validate_exist = self.uow.book.validate_book_exist_by_id(book_id=book_id)
        if not validate_exist:
            raise ValueError("Blog not exists")
        self.uow.book.delete(
            book_id=book_id,
        )


class UpdateBlogService:
    def __init__(
        self,
        uow: AbstractBookUnitOfWork,
    ):
        self.uow = uow

    def update(
        self,
        book_id: str,
        title: Optional[str] = None,
        author: Optional[str] = None,
        published_date: Optional[date] = None,
        genre: Optional[str] = None,
        price: Optional[float] = None,
    ) -> str:
        validate_object_id(id=book_id)
        validate_exist = self.uow.book.validate_book_exist_by_id(book_id=book_id)
        if not validate_exist:
            raise ValueError("Blog not exists")
        blog = self.uow.book.update(
            book_id=book_id,
            data=dict(
                title=title,
                author=author,
                published_date=published_date,
                genre=genre,
                price=Decimal(price) if price else None,
            ),
        )
        return blog


class GetAveragePriceBookService:
    def __init__(
        self,
        uow: AbstractBookUnitOfWork,
    ):
        self.uow = uow

    def get(
        self,
        year: int,
    ) -> str:
        average_year = self.uow.book.get_average_price_year(year=year)
        print(average_year)
        return average_year
