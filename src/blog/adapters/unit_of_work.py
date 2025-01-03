from src.blog.adapters.django_repository import BlogDjangoRepository

from src.blog.domain.repository import AbstractBlogUnitOfWork


class BlogUnitOfWork(AbstractBlogUnitOfWork):
    def __init__(self):
        self.users = BlogDjangoRepository()
