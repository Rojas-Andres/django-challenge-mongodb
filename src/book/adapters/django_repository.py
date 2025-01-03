from src.book.domain.repository import AbstractBookRepository
from django_apps.book.models import Book
from datetime import date


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
