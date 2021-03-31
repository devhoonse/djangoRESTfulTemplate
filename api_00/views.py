# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from api_00.serializers import UserSerializer, GroupSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
