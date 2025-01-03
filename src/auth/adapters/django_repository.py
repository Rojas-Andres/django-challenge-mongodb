from src.auth.domain.repository import AbstractUserRepository
from django_apps.user.models import User
from src.auth.domain import models


class UserDjangoRepository(AbstractUserRepository):
    def get_by_email(self, email):
        _user = User.objects.filter(email=email).first()
        return self.to_domain(_user) if _user else None

    def to_domain(self, model: User) -> models.User:
        user = models.User(
            id=model.pk,
            password=model.password,
            email=model.email,
            first_name=model.first_name,
            last_name=model.last_name,
            is_active=model.is_active,
            last_login=model.last_login,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )
        return user

    def get_by_id(self, user_id):
        _user = User.objects.filter(pk=user_id).first()
        return self.to_domain(_user) if _user else None

    def to_dict(self, user):
        return {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_active": user.is_active,
            "last_login": user.last_login,
            "created_at": user.created_at,
            "updated_at": user.updated_at,
        }
