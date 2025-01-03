from abc import ABC, abstractmethod
from typing import Any, Optional
from django.contrib.auth.hashers import make_password

# Standard Library
from abc import ABC, abstractmethod
from src.user.domain import models


class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[models.User]:
        raise NotImplementedError

    @abstractmethod
    def to_dict(self, user: models.User) -> dict:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[models.User]:
        raise NotImplementedError


class AbstractAuthUnitOfWork(ABC):
    users: AbstractUserRepository
