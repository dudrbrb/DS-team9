from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('join', views.join),
    path('login', views.login),
    path('list', views.list),
    path('mypage', views.mypage),
    path('myfriends', views.myfriends),
]