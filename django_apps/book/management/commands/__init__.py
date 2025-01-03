# Standard Library
import logging
from django.core.management.base import BaseCommand, CommandError
from django_apps.book.models import Book


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = """
        Creates a new aggregators

        Example of use:
    """

    def handle(self, *args, **options):
        logger.info(f"create_books ")

        # self.stdout.write(
        #     self.style.SUCCESS(f"Aggregator {aggregator_id.value} created.")
        # )
        # logger.info(
        #     f"create_aggregator :: aggregators {aggregator_id.value} created."
        # )
