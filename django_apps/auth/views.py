"""
File with the user views.
"""

# Standard Library
import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django_apps.utils.views.generic_decorators import GenerateSwagger
from django_apps.utils.views.mixins import APIErrorsMixin, LoggingRequestViewMixin
from src.auth.service_layer import services
from src.auth.adapters.unit_of_work import AuthUnitOfWork
from shared.adapters.token_libraries import JWTToken


logger = logging.getLogger(__name__)


@GenerateSwagger(swagger_auto_schema)
class AuthLoginView(LoggingRequestViewMixin, APIErrorsMixin, APIView):
    permission_classes = [AllowAny]

    class InputPostSerializer(serializers.Serializer):
        email = serializers.EmailField(max_length=255)
        password = serializers.CharField(max_length=100)

    class OutputPostSerializer(serializers.Serializer):
        token = serializers.CharField()

    def post(self, request):
        """
        AuthLoginView handles user login requests.

        This view allows users to log in by providing their email and password. It validates the input data, processes the login
        request using the LoginService, and returns a JWT token upon successful authentication.

        Attributes:
            permission_classes (list): A list of permission classes that determine access control for this view.
            InputPostSerializer (serializers.Serializer): A nested serializer class for validating input data.
            OutputPostSerializer (serializers.Serializer): A nested serializer class for formatting output data.

        Methods:
            post(request):
                Handles HTTP POST requests to authenticate a user and return a JWT token.

                Args:
                    request (Request): The HTTP request object containing user credentials.

                    Response: A response containing the JWT token if authentication is successful, or an error message if it fails.
        """
        input_serializer = self.InputPostSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        token = services.LoginService(
            uow=AuthUnitOfWork(), token_handler=JWTToken()
        ).login(**input_serializer.validated_data)
        output_data = self.OutputPostSerializer(data=dict(token=token))
        output_data.is_valid(raise_exception=True)
        return Response(data=output_data.validated_data, status=status.HTTP_200_OK)
