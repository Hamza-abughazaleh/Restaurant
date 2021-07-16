from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Reservation(models.Model):
    tableid = models.ForeignKey('table.Table', on_delete=models.CASCADE, related_name='table_reservation',)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str("Reservation {}").format(self.id)
