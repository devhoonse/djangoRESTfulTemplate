# -*- coding: utf-8 -*-


from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Records


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


# SERIALIZER FOR SAMPLE MODEL
class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('name', 'phone_number', 'address', 'created')
