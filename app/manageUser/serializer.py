from rest_framework import serializers
from .models import ManageUserModels


class ManageUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ManageUserModels
        fields = ('id', 'first_name', 'last_name', 'email', 'company')