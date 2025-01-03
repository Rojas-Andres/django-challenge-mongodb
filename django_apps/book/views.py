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
        price = serializers.DecimalField(max_digits=10, decimal_places=2)

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
        price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def post(self, request):
        input_serializer = self.InputPostSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        blog = services.CreateBlogService(uow=BlogUnitOfWork()).create(
            **input_serializer.validated_data
        )
        output_data = self.OutputPostSerializer(data=blog)
        output_data.is_valid(raise_exception=True)
        return Response(data=output_data.validated_data, status=status.HTTP_200_OK)
