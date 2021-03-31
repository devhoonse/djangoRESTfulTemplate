# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from rest_framework import viewsets

from api_00.models import Records
from api_00.serializers import UserSerializer, GroupSerializer, RecordsSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# VIEW FOR SAMPLE MODEL
class RecordsViewSet(viewsets.ModelViewSet):
    model = Records
    queryset = Records.objects.all().order_by('-created')
    serializer_class = RecordsSerializer
