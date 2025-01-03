# Standard Library
from enum import Enum


class TokenTypes(str, Enum):
    ACCESS = "access"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_
