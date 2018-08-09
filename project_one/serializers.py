from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import State, City
from datetime import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class StateSerializer(serializers.Serializer):
    id                = serializers.IntegerField()
    name              = serializers.CharField(max_length=50)
    abbr              = serializers.CharField(max_length=2)
    creation_date     = serializers.DateTimeField(default=datetime.now)
    last_update_date  = serializers.DateTimeField(default=datetime.now)

    class Meta:
        model=State
        fields = ('id', 'name', 'abbr', 'creation_date', 'last_update_date')


    def create(self, validated_data):
		return State.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id   = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.abbr = validated_data.get('abbr', instance.abbr)
        instance.last_update_date = validated_data.get('last_update_date', instance.last_update_date)
        instance.save()
        return instance

class CitySerializer(serializers.Serializer):
    class Meta:
        model=City
        fields = ('id', 'name', 'state_id', 'creation_date', 'last_update_date')

    def create(self, validated_data):
        print self
        return City.objects.create(**validated_data)
