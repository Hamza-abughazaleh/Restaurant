from rest_framework import serializers

from table.models import Table


# Serializers define the API representation.
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'userid', 'table_number', 'seats_number']

    def create(self, validated_data):
        table = super(TableSerializer, self).create(validated_data)
        table.table_number = validated_data['table_number']
        table.seats_number = validated_data['seats_number']
        table.userid = self.context['request'].user
        table.save()
        return table