from pynamodb.attributes import (
    JSONAttribute,
    NumberAttribute,
    UnicodeAttribute,
    UTCDateTimeAttribute,
)
from pynamodb.models import Model
from django.conf import settings


class IngressAPILog(Model):
    service_name = UnicodeAttribute(hash_key=True)
    timestamp = UTCDateTimeAttribute(range_key=True)
    http_method = UnicodeAttribute()
    request_data = JSONAttribute(null=True)
    response_data = JSONAttribute(null=True)
    error = UnicodeAttribute(null=True)
    status_code = NumberAttribute(null=True)

    class Meta:
        table_name = settings.DYNAMODB_INGRESS_API_LOG_TABLE_NAME


class EgressAPILog(IngressAPILog):
    class Meta:
        table_name = "EgressAPILog"
