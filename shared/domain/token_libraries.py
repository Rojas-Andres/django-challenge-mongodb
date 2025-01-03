from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Optional, TypeVar


Token = TypeVar("Token", bound=str)


class TokenHandler(ABC):
    @abstractmethod
    def encode(
        self,
        payload: dict[str, Any],
        algorithm: Optional[str] = None,
        expires: Optional[datetime] = None,
        **kwargs,
    ) -> Token:  # type: ignore
        """Register a token with parameters"""
        raise NotImplementedError("Encode method of TokenHandler not implemented")

    @abstractmethod
    def decode(self, token: str, **kwargs) -> dict[str, Any]:
        """Extract info from a signed object or token"""
        raise NotImplementedError("Decode method of TokenHandler not implemented")
