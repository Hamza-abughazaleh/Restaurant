from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from user.models import User


# Serializers define the API representation.
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'employee_number']

    def create(self, validated_data):
        user = super(UsersSerializer, self).create(validated_data)
        user.username = validated_data['username']
        user.employee_number = validated_data['employee_number']
        user.set_password(validated_data['password'])
        user.save()
        return user