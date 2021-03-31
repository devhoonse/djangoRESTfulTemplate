# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path, re_path
from api_00 import views as api_views


# 참고 : https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/#refactoring-to-use-viewsets
# 참고 : https://d-yong.tistory.com/61


app_name = 'api_00'
urlpatterns = [

    path('records/',
         api_views.RecordView.as_view(),
         name='index'),   # as_view 에 {'HTTP메서드': '뷰메서드'} dict 주자
    path('records/<str:rid>/',
         api_views.RecordView.as_view(),
         name='rid'),   # as_view 에 {'HTTP메서드': '뷰메서드'} dict 주자
]
