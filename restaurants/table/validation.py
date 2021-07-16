from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_table_seats(value):
    if value > settings.MAXIMUM_TABLE_SEATS_SIZE:
        raise ValidationError(
            _('%(value)s, table seats must be 12 or less'),
            params={'value': value},
        )
