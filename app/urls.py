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
    path('add_my_like/<str:my_like_username>/', views.Addmy_likeView.as_view(), name='add_my_like'),
    # path('add_you_liked/<str:you_liked_username>/', views.Addyou_likedView.as_view(), name='add_you_liked'),
    
    path('remove_friend/<str:friend_username>/', views.RemoveFriendView.as_view(), name='remove_friend'),
    path('remove_my_like/<str:my_like_username>/', views.Removemy_likeView.as_view(), name='remove_my_like'),
    path('remove_you_liked/<str:you_liked_username>/', views.Removeyou_likedView.as_view(), name='remove_you_liked'),
    
    path('auto_match_friends/', views.auto_match_friends, name='auto_match_friends'),

    path('board/post_list/', views.PostList.as_view()),
    path('board/<int:pk>/', views.PostDetail.as_view()),
    path('board/create_post/', views.PostCreate.as_view()),
    path('board/update_post/<int:pk>', views.PostUpdate.as_view()),

    path('comment_create/<int:pk>', views.comment_create, name='comment_create'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),

    path('list/list_search/', views.list_search, name='list_search'),
    path('post_search/', views.post_search, name='post_search'),
]