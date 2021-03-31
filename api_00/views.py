# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

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
class RecordsView(APIView):
    model = Records
    queryset = Records.objects.all().order_by('-created')
    serializer_class = RecordsSerializer

    def post(self, request):
        user_serializer = RecordsSerializer(data=request.data)  # Request 의 data 를 Serializer 로 변환

        if user_serializer.is_valid():
            user_serializer.save()  # Serializer 의 유효성 검사를 한 뒤 DB에 저장
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)  # client 에게 JSON response 전달
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('rid') is None:
            user_queryset = Records.objects.all()  # 모든 Record 의 정보를 불러온다.
            user_queryset_serializer = RecordsSerializer(user_queryset, many=True)
            return Response(user_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            rid = kwargs.get('rid')
            user_serializer = RecordsSerializer(Records.objects.get(rid=rid))  # rid 에 해당하는 Record 의 정보를 불러온다
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('rid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            rid = kwargs.get('rid')
            user_object = Records.objects.get(rid=rid)

            update_user_serializer = RecordsSerializer(user_object, data=request.data)
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('rid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            rid = kwargs.get('rid')
            user_object = Records.objects.get(rid=rid)
            user_object.delete()
            return Response("test ok", status=status.HTTP_200_OK)
