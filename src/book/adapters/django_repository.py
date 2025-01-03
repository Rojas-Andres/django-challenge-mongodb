from src.book.domain.repository import AbstractBookRepository
from django_apps.book.models import Book
from datetime import date
from django.db.models import Avg

from bson import ObjectId


class BookDjangoRepository(AbstractBookRepository):
    def create(
        self, title: str, author: str, published_date: str, genre: str, price: float
    ):
        book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            genre=genre,
            price=price,
        )
        return self.to_dict(book)

    def validate_book_exist(
        self, title: str, author: str, published_date: date, genre: str
    ) -> bool:
        books = Book.objects.filter(
            title=title,
            author=author,
            published_date=published_date,
            genre=genre,
        ).all()
        return [self.to_dict(book) for book in books]

    def to_dict(self, book: Book) -> dict:
        return {
            "title": book.title,
            "author": book.author,
            "published_date": book.published_date,
            "genre": book.genre,
            "price": book.price,
        }

    def validate_book_exist_by_id(self, book_id: str):
        book = Book.objects.filter(_id=ObjectId(book_id)).first()
        if book is None:
            return False
        return book

    def delete(self, book_id: str):
        book = Book.objects.filter(_id=ObjectId(book_id)).first()
        book.delete()

    def update(self, book_id: str, data: dict):
        book = Book.objects.filter(_id=ObjectId(book_id)).first()
        for key, value in data.items():
            if value is not None:
                setattr(book, key, value)
        book.save()
        return self.to_dict(book)

    def get_average_price_year(self, year: int) -> float:
        average = Book.objects.filter(published_date__year=year).aggregate(
            average_price=Avg("price")
        )["average_price"]
        return average
