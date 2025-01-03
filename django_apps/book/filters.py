from django_filters import rest_framework as filters

from django_apps.book.models import Book


class BookFilter(filters.FilterSet):
    _id = filters.CharFilter()
    title = filters.CharFilter()
    author = filters.CharFilter()

    class Meta:
        model = Book
        fields = ["_id", "title", "author"]
