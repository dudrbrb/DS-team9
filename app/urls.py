from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/delete/', views.delete, name='delete'),
    path('accounts/update/', views.update, name='update'),

    path('', views.Main.as_view()),
    path('list/', views.List.as_view()),
    path('mypage/', views.Mypage.as_view(), name='mypage'),
    path('friends/', views.Friends.as_view()),
    
    path('add_friend/<str:friend_username>/', views.AddFriendView.as_view(), name='add_friend'),
    path('remove_friend/<str:friend_username>/', views.RemoveFriendView.as_view(), name='remove_friend'),
    path('auto_match_friends/', views.auto_match_friends, name='auto_match_friends'),
]