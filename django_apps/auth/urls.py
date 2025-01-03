"""
File that contains the urls of the user app.
"""

from django.urls import path

from django_apps.auth.views import AuthLoginView

APP_NAME = "auth"

urlpatterns = [
    path("login/", AuthLoginView.as_view(), name="login"),
    # path("detail/", UserDetailView.as_view(), name="user_detail"),
]
