# -*- coding: utf-8 -*-

from django.urls import path, re_path
from api_00.views import RecordsViewSet


# 참고 : https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets


app_name = 'api_00'
url_patterns = [
    path('', RecordsViewSet.as_view(), name='index'),   # as_view 에 {'HTTP메서드': '뷰메서드'} dict 주자
    path('records/', RecordsViewSet.as_view(), name='records')
]
