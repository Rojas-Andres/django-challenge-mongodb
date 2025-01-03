from src.user.adapters.django_repository import UserDjangoRepository

# from src.shared.domain.service_layer import unit_of_work
from django_apps.utils.adapters import unit_of_work
from src.user.domain.repository import AbstractUserUnitOfWork


class UserUnitOfWork(AbstractUserUnitOfWork):
    def __init__(self):
        self.users = UserDjangoRepository()
