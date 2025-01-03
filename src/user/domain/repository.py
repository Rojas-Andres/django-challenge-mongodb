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


class AbstractUserUnitOfWork(ABC):
    users: AbstractUserRepository
