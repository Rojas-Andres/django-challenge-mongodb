from bson import ObjectId


def validate_object_id(id: str):
    if not ObjectId.is_valid(id):
        raise ValueError("Invalid ObjectId")
    return id
