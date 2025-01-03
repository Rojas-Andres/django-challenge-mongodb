import copy
from datetime import datetime
from typing import Any, Dict

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpRequest
from rest_framework import exceptions as rest_exceptions
from rest_framework import status
from rest_framework.response import Response

from django_apps.utils.views.exceptions import Throttled

from shared.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from shared.utils.core.json import prepare_data_for_json_serialization
from shared.utils.core.sensible import obfuscate_sensible_data
from shared.utils.core.logging.models import IngressAPILog
from pymongo.errors import NetworkTimeout, ServerSelectionTimeoutError


class NetworkTimeoutDB(rest_exceptions.APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Network Timeout RECUERDE es una capa gratuita de mongo y eso se cae cada 10 segundos, pruebe mejor local con docker-compose el proyecto"
    default_code = "error_connection_mongo"


class ServerSelectionTimeoutErrorDB(rest_exceptions.APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Network Timeout RECUERDE es una capa gratuita de mongo y eso se cae cada 10 segundos, pruebe mejor local con docker-compose el proyecto"
    default_code = "error_connection_mongo"


class Base:
    """
    Mixin that transforms Django and Python exceptions into rest_framework ones
    without the mixin, they return 500 status code which is not desired.
    """

    expected_exceptions = {
        AssertionError: rest_exceptions.APIException,
        ValueError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied,
        ObjectDoesNotExist: rest_exceptions.NotFound,
        ValidationError: rest_exceptions.ValidationError,
        NetworkTimeout: NetworkTimeoutDB,
        ServerSelectionTimeoutError: ServerSelectionTimeoutErrorDB,
    }

    def handle_exception(self, exc):
        exception_ancestors = exc.__class__.__mro__[:-1]  # Without `object`

        for ancestor_class in exception_ancestors:
            drf_exception_class = self.expected_exceptions.get(ancestor_class)

            if drf_exception_class is None:
                continue

            drf_exception = drf_exception_class(self.get_error_message(exc))

            return super().handle_exception(drf_exception)

        return super().handle_exception(exc)

    def get_first_matching_attr(self, obj, *attrs, default=None):
        for attr in attrs:
            if hasattr(obj, attr):
                return getattr(obj, attr)

        return default

    def get_error_message(self, exc):
        if hasattr(exc, "message_dict"):
            return exc.message_dict
        error_msg = self.get_first_matching_attr(exc, "message", "messages")

        if isinstance(error_msg, list):
            error_msg = ", ".join(error_msg)

        if error_msg is None:
            error_msg = str(exc)
        return {"errors": [error_msg]}


class APIErrorsMixin(Base):
    Base.expected_exceptions = {
        ObjectDoesNotExist: rest_exceptions.NotFound,
        **Base.expected_exceptions,
    }


class LoggingRequestViewMixin:
    """Mixin that log the request and response on DynamoDB table.

    Attributes:
        sensible_keys: A list of strings.
            Each element is going to be obfuscated.
    """

    sensible_keys = ["password", "token"]

    def finalize_response(self, request, response, *args, **kwargs):
        try:
            service_name = request.path
            request_data = copy.deepcopy(request.data)
            http_method = request.method
            status_code = response.status_code
            response_data = copy.deepcopy(response.data)

            obfuscate_sensible_data(sensible_keys=self.sensible_keys, data=request_data)
            obfuscate_sensible_data(
                sensible_keys=self.sensible_keys, data=response_data
            )

            internal_api_log_data = {
                "service_name": service_name,
                "http_method": http_method,
                "request_data": request_data,
            }
            self._internal_api_log(
                **internal_api_log_data,
                response_data=response_data,
                status_code=status_code,
            )
        except Exception as e:
            print(f"Error while logging request and response: {e}")
            # send slack error message
        return super().finalize_response(request, response, *args, **kwargs)

    def _internal_api_log(
        self,
        *,
        service_name: str,
        http_method: str,
        request_data: Dict[str, Any] = None,
        response_data: Dict[str, Any] = None,
        status_code: int = None,
        error: str = None,
    ) -> None:
        if request_data:
            prepare_data_for_json_serialization(data=request_data)
        if response_data:
            prepare_data_for_json_serialization(data=response_data)
        timestamp = datetime.utcnow()
        internal_log = IngressAPILog(
            service_name=service_name,
            timestamp=timestamp,
            http_method=http_method,
            request_data=request_data,
            response_data=response_data,
            error=error,
            status_code=status_code,
        )
        internal_log.save()
