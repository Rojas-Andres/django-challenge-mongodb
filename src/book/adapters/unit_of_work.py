from src.book.adapters.django_repository import BookDjangoRepository

from src.book.domain.repository import AbstractBookUnitOfWork


class BlogUnitOfWork(AbstractBookUnitOfWork):
    def __init__(self):
        self.book = BookDjangoRepository()
