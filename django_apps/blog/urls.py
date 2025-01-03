"""
File that contains the urls of the user app.
"""

from django.urls import path

from django_apps.blog.views import CreateBlogView

APP_NAME = "blog"

urlpatterns = [
    path("", CreateBlogView.as_view(), name="create_blog_view"),
    # path("detail/", UserDetailView.as_view(), name="user_detail"),
]
