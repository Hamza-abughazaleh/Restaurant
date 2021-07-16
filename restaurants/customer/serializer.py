from django.conf import settings
from rest_framework import serializers
from table.models import Table
from table.service import get_table_time_slots_available


# Serializers define the API representation.
class CustomerTableSerializer(serializers.ModelSerializer):
    time_slots = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = ['id', 'seats_number', 'table_number', 'time_slots']

    def get_time_slots(self, table):
        return get_table_time_slots_available(table)
