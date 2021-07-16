from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_employee_number(value):
    if len(str(value)) != settings.EMPLOYEE_NUMBER_DIGITS_SIZE:
        raise ValidationError(
            _('%(value)s, employee number must be 4 digits'),
            params={'value': value},
        )
