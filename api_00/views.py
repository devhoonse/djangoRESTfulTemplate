# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_00.models import Record
from api_00.serializers import UserSerializer, GroupSerializer, RecordSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# VIEW FOR SAMPLE MODEL
class RecordView(APIView):
    model = Record
    queryset = Record.objects.all().order_by('-created')
    serializer_class = RecordSerializer

    def post(self, request):
        serializer = RecordSerializer(data=request.data)  # Request 의 data 를 Serializer 로 변환

        if serializer.is_valid():
            serializer.save()  # Serializer 의 유효성 검사를 한 뒤 DB에 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # client 에게 JSON response 전달
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('rid') is None:
            queryset = Record.objects.all()  # 모든 Record 의 정보를 불러온다.
            queryset_serializer = RecordSerializer(queryset, many=True)
            return Response(queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            rid = kwargs.get('rid')
            serializer = RecordSerializer(Record.objects.get(rid=rid))  # rid 에 해당하는 Record 의 정보를 불러온다
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, **kwargs):
        if kwargs.get('rid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            rid = kwargs.get('rid')
            record_object = Record.objects.get(rid=rid)

            serializer = RecordSerializer(record_object, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('rid') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            rid = kwargs.get('rid')
            record_object = Record.objects.get(rid=rid)
            record_object.delete()
            return Response("test ok", status=status.HTTP_200_OK)
