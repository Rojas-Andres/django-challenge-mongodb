from src.blog.domain.repository import AbstractBlogUnitOfWork


class CreateBlogService:
    def __init__(
        self,
        uow: AbstractBlogUnitOfWork,
    ):
        self.uow = uow

    def create(
        self,
        title: str,
        author: str,
        published_date: str,
        genre: str,
        price: float,
    ) -> str:
        return "Blog created successfully"
