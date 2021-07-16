from django.db import models
from django.utils.translation import gettext_lazy as _

from .validation import validate_table_seats


# Create your models here.
class Table(models.Model):
    userid = models.ForeignKey('user.User', null=True, on_delete=models.SET_NULL)
    table_number = models.IntegerField(
        _('Employee number'),
        unique=True,
        error_messages={
            'unique': _("A Table number already exists."),
        }
    )
    seats_number = models.IntegerField(
        _('Employee number'),
        validators=[validate_table_seats]
    )

    def __str__(self):
        return str("Table Number {}").format(self.table_number)
