from enum import Enum
from typing import Any
from bson import ObjectId


def enum_to_choices(obj: type[Enum]) -> list[tuple[Any, str]]:
    return [(elem.value, elem.name) for elem in iter(obj)]  # type: ignore


def validate_object_id(id: str):
    if not ObjectId.is_valid(id):
        raise ValueError("Invalid id")
    return id
