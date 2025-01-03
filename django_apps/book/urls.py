"""
File that contains the urls of the user app.
"""

from django.urls import path

from django_apps.book.views import CreateBookView, DeleteBookView

APP_NAME = "book"

urlpatterns = [
    path("", CreateBookView.as_view(), name="create_book_view"),
    # add path to delete book view with id
    path("<str:book_id>", DeleteBookView.as_view(), name="delete_book_view"),
]
