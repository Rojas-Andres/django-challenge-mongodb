"""
File that contains the urls of the user app.
"""

from django.urls import path

from django_apps.book.views import (
    CreateBookView,
    DeleteBookView,
    BookListView,
    UpdateBookView,
)

APP_NAME = "book"

urlpatterns = [
    path("", CreateBookView.as_view(), name="create_book_view"),
    path("list", BookListView.as_view(), name="list_book_view"),
    path("<str:book_id>", UpdateBookView.as_view(), name="patch_book_view"),
    path("<str:book_id>", DeleteBookView.as_view(), name="delete_book_view"),
]
