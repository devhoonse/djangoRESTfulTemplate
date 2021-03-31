# -*- coding: utf-8 -*-

from django.urls import path, re_path
from api_00.views import RecordsView


app_name = 'api_00'
url_patterns = [
    path('', RecordsView.as_view(), name='index'),
    path('records/', RecordsView.as_view(), name='records')
]
