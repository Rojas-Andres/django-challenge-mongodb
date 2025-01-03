from abc import ABC, abstractmethod

# Standard Library
from abc import ABC, abstractmethod


class AbstractBlogRepository(ABC):
    @abstractmethod
    def create(self, title: str):
        raise NotImplementedError


class AbstractBlogUnitOfWork(ABC):
    blog: AbstractBlogRepository
