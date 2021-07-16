from datetime import datetime

from django.conf import settings
from reservation.models import Reservation
from rest_framework import serializers


# Serializers define the API representation.
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'tableid', 'date', 'start_time', 'end_time']

    def validate(self, data):
        if Reservation._default_manager.filter(tableid=data['tableid'], date=data["date"],
                                               start_time=data['start_time'],
                                               end_time=data['end_time']).exists():
            raise serializers.ValidationError("This time was reservation for this table")
        if data['date'] == datetime.now().date() and (
                data['start_time'] < datetime.now().time() or data['start_time'] < datetime.now().time()):
            raise serializers.ValidationError(
                "Please select time grater than {}".format(datetime.now().time().strftime('%H:%M')))
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("Start time must be less than end time")
        if data['end_time'] <= data['start_time']:
            raise serializers.ValidationError("end time must be greater than start time")
        if data['end_time'] > settings.RESTAURANT_TIME_CLOSE or data['start_time'] < settings.RESTAURANT_TIME_OPEN:
            raise serializers.ValidationError(
                "The restaurant open at {} end close at {} so please select time between them".format(
                    settings.RESTAURANT_TIME_OPEN.strftime('%H:%M'), settings.RESTAURANT_TIME_CLOSE.strftime('%H:%M')))
        return data

    def create(self, validated_data):
        reservation = super(ReservationSerializer, self).create(validated_data)
        reservation.date = validated_data['date']
        reservation.start_time = validated_data['start_time']
        reservation.end_time = validated_data['end_time']
        reservation.tableid = validated_data['tableid']
        reservation.save()
        return reservation
