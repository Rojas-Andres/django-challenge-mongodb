"""
File with the blog views.
"""

# Standard Library
import logging
from django.utils import timezone
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from django_apps.utils.views.generic_decorators import GenerateSwagger
from django_apps.utils.views.mixins import APIErrorsMixin, LoggingRequestViewMixin

from src.auth.adapters.django_authenticator import TokenAuthentication
from src.book.service_layer import services
from src.book.adapters.unit_of_work import BlogUnitOfWork
from django_apps.utils.views.generic_views import ListCoreView
from django_apps.book.models import Book
from django_apps.utils.views.pagination import CorePagination
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_apps.book.filters import BookFilter

logger = logging.getLogger(__name__)


@GenerateSwagger(swagger_auto_schema)
class CreateBookView(LoggingRequestViewMixin, APIErrorsMixin, APIView):
    sensible_keys = ("token",)
    authentication_classes = (TokenAuthentication,)

    class InputPostSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=255)
        author = serializers.CharField(max_length=255)
        published_date = serializers.DateField()
        genre = serializers.CharField(max_length=100)
        price = serializers.IntegerField()

        def validate_published_date(self, value):
            if value > timezone.now().date():
                raise serializers.ValidationError(
                    "Published date no puede ser en el futuro"
                )
            return value

    class OutputPostSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=255)
        author = serializers.CharField(max_length=255)
        published_date = serializers.DateField()
        genre = serializers.CharField(max_length=100)
        price = serializers.IntegerField()

    def post(self, request):
        input_serializer = self.InputPostSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        blog = services.CreateBlogService(uow=BlogUnitOfWork()).create(
            **input_serializer.validated_data
        )
        output_data = self.OutputPostSerializer(data=blog)
        output_data.is_valid(raise_exception=True)
        return Response(data=output_data.validated_data, status=status.HTTP_200_OK)


@GenerateSwagger(swagger_auto_schema)
class DeleteBookView(LoggingRequestViewMixin, APIErrorsMixin, APIView):
    sensible_keys = ("token",)
    authentication_classes = (TokenAuthentication,)

    class InputDeleteSerializer(serializers.Serializer):
        book_id = serializers.CharField(max_length=255)

    class OutputPostSerializer(serializers.Serializer): ...

    def delete(self, request, book_id):
        input_serializer = self.InputDeleteSerializer(data=dict(book_id=book_id))
        input_serializer.is_valid(raise_exception=True)
        services.DeleteBlogService(uow=BlogUnitOfWork()).delete(
            **input_serializer.validated_data
        )
        return Response(
            data={"message": "Book deleted successfully"}, status=status.HTTP_200_OK
        )


@GenerateSwagger(swagger_auto_schema)
class BookListView(APIErrorsMixin, ListCoreView):
    """
    A view for retrieving a list of all users.
    Requires authentication to access the view.
    """

    sensible_keys = ("token",)
    authentication_classes = (TokenAuthentication,)

    class OutputGetSerializer(serializers.Serializer):
        _id = serializers.CharField()
        title = serializers.CharField(allow_null=True)
        author = serializers.CharField(allow_null=True)
        published_date = serializers.DateField(allow_null=True)
        genre = serializers.ImageField(allow_null=True)
        price = serializers.IntegerField()

    serializer_class = OutputGetSerializer
    queryset = Book.objects.all()
    pagination_class = CorePagination
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_class = BookFilter


@GenerateSwagger(swagger_auto_schema)
class UpdateBookView(LoggingRequestViewMixin, APIErrorsMixin, APIView):
    sensible_keys = ("token",)
    authentication_classes = (TokenAuthentication,)

    class InputPatchSerializer(serializers.Serializer):
        title = serializers.CharField(required=False, max_length=255)
        author = serializers.CharField(required=False, max_length=255)
        published_date = serializers.DateField(required=False)
        genre = serializers.CharField(required=False, max_length=100)
        price = serializers.IntegerField(
            required=False,
        )

        def validate_published_date(self, value):
            if value > timezone.now().date():
                raise serializers.ValidationError(
                    "Published date no puede ser en el futuro"
                )
            return value

    class OutputPatchSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=255)
        author = serializers.CharField(max_length=255)
        published_date = serializers.DateField()
        genre = serializers.CharField(max_length=100)
        price = serializers.IntegerField()

    def patch(self, request, book_id):
        input_serializer = self.InputPatchSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        blog = services.UpdateBlogService(uow=BlogUnitOfWork()).update(
            **input_serializer.validated_data, book_id=book_id
        )
        output_data = self.OutputPatchSerializer(data=blog)
        output_data.is_valid(raise_exception=True)
        return Response(data=output_data.validated_data, status=status.HTTP_200_OK)


@GenerateSwagger(swagger_auto_schema)
class BookAverageYearView(APIErrorsMixin, APIView):
    """
    A view for retrieving a list of all users.
    Requires authentication to access the view.
    """

    sensible_keys = ("token",)
    authentication_classes = (TokenAuthentication,)

    class InputGetSerializer(serializers.Serializer):
        year = serializers.IntegerField(required=True)

        def validate_year(self, value):
            if value > timezone.now().year:
                raise serializers.ValidationError("Year cannot be in the future")
            if value < 1900:
                raise serializers.ValidationError("Year cannot be before 1900")
            return value

    class OutputGetSerializer(serializers.Serializer):
        average = serializers.FloatField(required=True)

    def get(self, request):
        input_serializer = self.InputGetSerializer(data=request.query_params)
        input_serializer.is_valid(raise_exception=True)
        average = services.GetAveragePriceBookService(uow=BlogUnitOfWork()).get(
            **input_serializer.validated_data
        )
        output_data = self.OutputGetSerializer(data=dict(average=average))
        output_data.is_valid(raise_exception=True)
        return Response(data=output_data.validated_data, status=status.HTTP_200_OK)
