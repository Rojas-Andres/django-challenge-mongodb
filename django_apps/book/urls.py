"""
File that contains the urls of the user app.
"""

from django.urls import path

from django_apps.book.views import CreateBookView

APP_NAME = "book"

urlpatterns = [
    path("", CreateBookView.as_view(), name="create_book_view"),
    # path("detail/", UserDetailView.as_view(), name="user_detail"),
]
