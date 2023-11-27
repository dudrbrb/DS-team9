from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view()),
    path('join/', views.Join.as_view()),
    path('list/', views.List.as_view()),
    path('mypage/<int:pk>/', views.Mypage.as_view()),
    path('friends/', views.Friends.as_view()),


    path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    
    path('logout/', LogoutView.as_view(), name='logout'), 
]