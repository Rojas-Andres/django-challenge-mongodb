from src.blog.domain.repository import AbstractBlogRepository


class BlogDjangoRepository(AbstractBlogRepository):
    def create(self, title): ...
