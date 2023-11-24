from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view()),
    path('join/', views.Join.as_view()),
    path('list/', views.List.as_view()),
    path('mypage/', views.Mypage.as_view()),
    path('friends/', views.Friends.as_view()),

    # 로그인, 로그아웃은 views 없이 구현
    path('login/', LoginView.as_view(template_name='login.html'), name='login'), 
    # 템플릿 지정만 파라미터로 넘겨주면 끝
    path('logout/', LogoutView.as_view(), name='logout'), 
]