# Standard Library
from abc import ABC, abstractmethod
from typing import Any, Optional, cast

# Django
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.request import Request

# Internal
from shared.adapters.token_libraries import JWTToken as JWTTokenService
from shared.domain.constants import TokenTypes
from shared.exceptions import InvalidTokenError, TokenExpiredError

from shared.domain.token_libraries import TokenHandler as TokenLibraryInterface

from src.auth.domain.repository import AbstractUserRepository

from src.auth.adapters.django_repository import UserDjangoRepository

from src.auth.domain.models import User


class CredentialsAuthenticator(ABC):
    authentication_failure_message: str
    allowed_token_types: list[str]

    def __init__(self, repository, token_handler: TokenLibraryInterface):
        self.repository = repository
        self.token_handler = token_handler

    def authenticate(self, request: Any, **kwargs):
        """Authenticate and extract user if it is app_cclicable"""
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise NotAuthenticated("Token not provided")

        try:
            payload = self.token_handler.decode(token)
        except TokenExpiredError:
            raise AuthenticationFailed("Token expired.")
        except InvalidTokenError as e:
            raise AuthenticationFailed(f"Invalid token: {str(e)}")
        except Exception as e:
            raise AuthenticationFailed(f"Token error: {str(e)}")

        if not payload.get("typ") in self.allowed_token_types:
            raise AuthenticationFailed("Invalid token")

        user_id = cast(str, payload.get("user_id"))
        user = self.authenticate_credentials(user_id)

        return user, token

    def authenticate_header(self, request):
        """Sets WWW-Authenticate header value for unauthorized responses."""

        return self.authentication_failure_message

    @abstractmethod
    def authenticate_credentials(self, _id: str):
        """handle token claims to return a domain user"""


class TokenAuthentication(CredentialsAuthenticator):
    authentication_failure_message = "Missing or invalid token."
    allowed_token_types = [TokenTypes.ACCESS]
    repository: AbstractUserRepository

    def __init__(
        self,
        repository: Optional[AbstractUserRepository] = None,
        token_handler: Optional[TokenLibraryInterface] = None,
    ):
        super().__init__(
            repository or UserDjangoRepository(),
            token_handler or JWTTokenService(),
        )

    def authenticate_credentials(self, _id: str) -> Optional[User]:
        user = self.repository.get_by_id(user_id=_id)
        if not user:
            raise AuthenticationFailed("Invalid credentials")

        return user
