from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validation import validate_employee_number


# Create your models here.
class User(AbstractUser):
    employee_number = models.IntegerField(
        _('Employee number'),
        unique=True,
        validators=[AbstractUser.username_validator, validate_employee_number],
        error_messages={
            'unique': _("A user with that Employee number already exists."),
        },
    )
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'employee_number'

    def __str__(self):
        return str(self.username)
