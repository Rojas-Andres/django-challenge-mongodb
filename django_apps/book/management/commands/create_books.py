# Standard Library
import logging
from django.core.management.base import BaseCommand, CommandError
from django_apps.book.models import Book
from faker import Faker

logger = logging.getLogger(__name__)

fake = Faker()


class Command(BaseCommand):
    help = """ Creates a new books """

    def handle(self, *args, **options):
        logger.info(f"create_books ")
        for _ in range(5):
            book = Book.objects.create(
                title=fake.user_name(),
                author=fake.first_name(),
                published_date="2023-04-12",
                genre="genre",
                price=1233,
            )
            book.save()
            self.stdout.write(self.style.SUCCESS(f"Book {book.title} created."))
        self.stdout.write(self.style.SUCCESS("Books created."))
