from src.auth.adapters.django_repository import UserDjangoRepository

from src.auth.domain.repository import AbstractAuthUnitOfWork


class AuthUnitOfWork(AbstractAuthUnitOfWork):
    def __init__(self):
        self.users = UserDjangoRepository()
