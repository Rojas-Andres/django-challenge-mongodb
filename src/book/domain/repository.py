from abc import ABC, abstractmethod


class AbstractBookRepository(ABC):
    @abstractmethod
    def create(
        self, title: str, author: str, published_date: str, genre: str, price: float
    ):
        raise NotImplementedError

    @abstractmethod
    def validate_book_exist(
        self, title: str, author: str, published_date: str, genre: str
    ):
        raise NotImplementedError


class AbstractBookUnitOfWork(ABC):
    book: AbstractBookRepository