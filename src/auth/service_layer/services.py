from datetime import timedelta

from src.auth.domain.repository import AbstractAuthUnitOfWork
from src.auth.domain import models
from django.contrib.auth.hashers import check_password
from shared.domain.token_libraries import TokenHandler
from django.conf import settings
from django.utils import timezone


class LoginService:
    def __init__(
        self,
        uow: AbstractAuthUnitOfWork,
        token_handler: TokenHandler,
    ):
        self.uow = uow
        self.token_handler = token_handler

    def login(
        self,
        email: str,
        password: str,
    ) -> str:
        user = self.uow.users.get_by_email(email)
        if not user:
            raise ValueError("User not found")
        if not check_password(password, user.password):
            raise ValueError("Invalid password")
        token = self.__create_token(user_id=user.id)
        return token

    def __create_token(self, user_id: int) -> str:
        to_expire = timedelta(minutes=settings.TOKEN_MINUTES_EXPIRATION)
        return self.token_handler.encode(
            payload={
                "user_id": user_id,
            },
            expires=timezone.now() + to_expire,
        )
