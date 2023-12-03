from rest_framework import serializers
from utils.serializer_fields import QuerySetField
from user.models import User


class UserBlockSerializer(serializers.ModelSerializer):
    blocked_users = QuerySetField(queryset=User.objects.all())

    class Meta:
        model = User
        fields = ['blocked_users']