# app/views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm, PostForm, CommentForm
from .models import Post, Major1, Major2, Tag, User, Comment
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import View
from django.db.models import Q  
from django.urls import reverse_lazy



def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # 인스턴스를 바로 저장하지 않음
            user.prof_image = form.cleaned_data['prof_image']
            user.back_image = form.cleaned_data['back_image']
            user.save()

            user.tag.set(form.cleaned_data['tag'])
            auth_login(request, form.get_user())
            return redirect("/")
        
    else:
        form = CustomUserCreationForm()

    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("/")
        
    else:
        form = CustomAuthenticationForm()

    context = {'form' : form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('/')

def delete(request):
    user = request.user
    user.delete()
    return redirect('/')

def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)  # 인스턴스를 바로 저장하지 않음
            user.tag.set(form.cleaned_data['tag'])
            user.prof_image = form.cleaned_data['prof_image']
            user.back_image = form.cleaned_data['back_image']
            user.save()
            return redirect("/mypage")
        
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {'form' : form}
    return render(request, 'accounts/update.html', context)



class Main(ListView):
    model = get_user_model() 
    ordering = '-pk'
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data()

        return context


class List(ListView):
    model = get_user_model() 
    ordering = '-pk'
    template_name = 'list.html'

    def get_queryset(self):
        return self.model.objects.filter(open_profile=True)

class Mypage(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'mypage.html'

    def get_object(self, queryset=None):
        return self.request.user

class Friends(ListView):
    model = get_user_model()
    ordering = '-pk'
    template_name = 'friends.html'

    def get_context_data(self, *args, **kwargs):
        user_instance = self.request.user  # 현재 로그인한 사용자 객체 가져오기

        friends_usernames = user_instance.friends.split('/')
        my_like_usernames = user_instance.my_like.split('/')
        you_liked_usernames = user_instance.you_liked.split('/')

        friends_users = User.objects.filter(username__in=friends_usernames)
        my_like_users = User.objects.filter(username__in=my_like_usernames)
        you_liked_users = User.objects.filter(username__in=you_liked_usernames)

        context = {
            'friends_users': friends_users, 
            'my_like_users': my_like_users, 
            'you_liked_users': you_liked_users,
            }
        return context

class Addmy_likeView(LoginRequiredMixin, View):
    def get(self, request, my_like_username, *args, **kwargs):
        my_like = get_object_or_404(get_user_model(), username=my_like_username)
        user_instance = self.request.user

        # 현재 사용자의 my_like 목록에 상대방 추가
        user_instance.my_like += f'/{my_like_username}'
        user_instance.save()

        # 상대방의 you_liked 목록에 현재 사용자 추가
        my_like.you_liked += f'/{user_instance.username}'
        my_like.save()

        messages.success(self.request, f'{my_like_username}님에게 친구 요청을 보냈습니다.')

        return redirect('/friends')


class Removemy_likeView(LoginRequiredMixin, View):
    def get(self, request, my_like_username, *args, **kwargs):
        my_like = get_object_or_404(get_user_model(), username=my_like_username)
        user_instance = self.request.user

        # 현재 사용자의 my_like를 삭제하고 저장
        user_instance.my_like = '/'.join([my_like_name for my_like_name in user_instance.my_like.split('/') if my_like_name != my_like_username])
        user_instance.save()

        # 상대방의 you_liked를 삭제하고 저장
        my_like.you_liked = '/'.join([you_liked_name for you_liked_name in my_like.you_liked.split('/') if you_liked_name != user_instance.username])
        my_like.save()


        messages.success(self.request, f'{my_like.username}님에게 보내는 요청을 취소했습니다.')
        return redirect('/friends')


# class Addyou_likedView(LoginRequiredMixin, View):
#     def get(self, request, you_liked_username, *args, **kwargs):
#         you_liked = get_object_or_404(get_user_model(), username=you_liked_username)
#         user_instance = self.request.user

#         # 이미 you_liked 목록에 있는지 확인
#         if you_liked.username not in user_instance.you_liked:
#             #you_liked에 추가
#             user_instance.you_liked += f'/{you_liked.username}'
#             user_instance.save()
#             messages.success(self.request, f'{you_liked.username}님에게 친구 요청을 받았습니다.')
#         else:
#             messages.warning(self.request, f'{you_liked.username}님은 이미 친구입니다.')

#         return redirect('/friends')

class Removeyou_likedView(LoginRequiredMixin, View):
    def get(self, request, you_liked_username, *args, **kwargs):
        you_liked = get_object_or_404(get_user_model(), username=you_liked_username)
        user_instance = self.request.user

        # 현재 사용자의 you_liked를 삭제하고 저장
        user_instance.you_liked = '/'.join([you_liked_name for you_liked_name in user_instance.you_liked.split('/') if you_liked_name != you_liked_username])
        user_instance.save()

        # 상대방의 my_like를 삭제하고 저장
        you_liked.my_like = '/'.join([my_like_name for my_like_name in you_liked.my_like.split('/') if my_like_name != user_instance.username])
        you_liked.save()

        messages.success(self.request, f'{you_liked.username}님의 요청을 거절했습니다.')
        return redirect('/friends')

# class RemoveFriendView(LoginRequiredMixin, View):
#     def get(self, request, friend_username, *args, **kwargs):
#         friend = get_object_or_404(get_user_model(), username=friend_username)
#         user_instance = self.request.user

#         # 현재 사용자의 friends를 삭제하고 저장
#         user_instance.friends = '/'.join([friend_name for friend_name in user_instance.friends.split('/') if friend_name != friend_username])
#         user_instance.save()

#         # 상대방의 friends를 삭제하고 저장
#         friend.friends = '/'.join([friend_name for friend_name in friend.friends.split('/') if friend_name != user_instance.username])
#         friend.save()

#         messages.success(self.request, f'{friend.username}님을 친구에서 삭제했습니다.')
#         return redirect('/friends')

class AddFriendView(LoginRequiredMixin, View):
    def get(self, request, friend_username, *args, **kwargs):
        friend = get_object_or_404(get_user_model(), username=friend_username)
        user_instance = self.request.user

        # 이미 친구 목록에 있는지 확인
        if friend.username not in user_instance.friends:
            # 현재 사용자의 you_liked를 삭제
            user_instance.you_liked = '/'.join([you_liked_name for you_liked_name in user_instance.you_liked.split('/') if you_liked_name != friend_username])
            user_instance.save()

            # 상대방의 my_like를 삭제
            friend.my_like = '/'.join([my_like_name for my_like_name in friend.my_like.split('/') if my_like_name != user_instance.username])
            friend.save()

            # 상대방의 friends에 추가하고 저장
            friend.friends += f'/{user_instance.username}'
            friend.save()

            # 현재 사용자의 friends 추가하고 저장
            user_instance.friends += f'/{friend.username}'
            user_instance.save()
            messages.success(self.request, f'{friend.username}님을 친구로 추가했습니다.')
        else:
            messages.warning(self.request, f'{friend.username}님은 이미 친구입니다.')

        return redirect('/friends')

class RemoveFriendView(LoginRequiredMixin, View):
    def get(self, request, friend_username, *args, **kwargs):
        friend = get_object_or_404(get_user_model(), username=friend_username)
        user_instance = self.request.user

        # 현재 사용자의 friends를 삭제하고 저장
        user_instance.friends = '/'.join([friend_name for friend_name in user_instance.friends.split('/') if friend_name != friend_username])
        user_instance.save()

        # 상대방의 friends를 삭제하고 저장
        friend.friends = '/'.join([friend_name for friend_name in friend.friends.split('/') if friend_name != user_instance.username])
        friend.save()

        messages.success(self.request, f'{friend.username}님을 친구에서 삭제했습니다.')
        return redirect('/friends')


# 자동 매칭

def auto_match_friends(request):
    # 현재 로그인한 사용자 정보 가져오기
    user_profile = User.objects.get(id=request.user.id)
    user_tags = user_profile.tag.all()

    matching_threshold = 2

    # 사용자 본인을 제외한 모든 사용자 가져오기
    all_users = User.objects.exclude(id=request.user.id)

    # 유사한 친구를 담을 리스트
    matched_friends = []

    # 모든 사용자에 대해 검사
    for friend in all_users:
        # 사용자의 해시태그 중 공통된 것만 가져오기
        common_tags = friend.tag.filter(id__in=user_tags)
        
        # 해시태그 개수가 기준 이상으로 유사하면 추가
        if common_tags.count() >= matching_threshold:
            matched_friends.append({
                'friend': friend,
                'common_tags': common_tags
            })

    context = {'matched_friends': matched_friends}
    return render(request, 'auto_match_friends.html', context)


#게시판

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'board/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'board/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post_id=post.id)  # 필터링하여 해당 게시물의 댓글 가져오기
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context


class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'board/post_form.html'
    form_class = PostForm

    def test_func(self):
        return True
    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated :
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/board/post_list')


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'board/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:   
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def comment_create(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # 댓글 작성자를 현재 로그인한 사용자로 설정
            comment.save()
            return redirect('/board/'+str(pk), pk=pk)
    else:
        form = CommentForm()

    return redirect('/board/'+str(pk) , pk=pk)


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        pk = comment.post_id
        comment.post = None  # 댓글이 속한 게시물을 제거하고
        comment.delete()     # 댓글 삭제
        return redirect('/board/' + str(pk))

    return redirect('/board/' + str(pk))


# list 중 검색
def list_search(request):
    query = request.GET.get('q')

    if query:
        results = User.objects.filter(
            Q(nickname__icontains=query) |  # 이름에서 검색
            Q(tag__name__icontains=query) |  # 해시태그에서 검색
            Q(major1__icontains=query) |  # 학과1에서 검색
            Q(major2__icontains=query),  # 학과2에서 검색
            open_profile=True
        ).distinct()
    else:
        results = User.objects.none()

    return render(request, 'list.html', {'object_list': results, 'query': query})

#post 중 검색

def post_search(request):
    query = request.GET.get('q')

    if query:
        # Post 모델의 title과 content에서 검색, 작성자는 username으로 검색
        results = Post.objects.filter(
            Q(title__icontains=query) |  # 제목에서 검색
            Q(author__username__icontains=query),  # 작성자의 username에서 검색
        )
    else:
        results = Post.objects.none()

    return render(request, 'board/post_list.html', {'post_list': results, 'query': query})