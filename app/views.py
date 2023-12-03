from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView,TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   # 로그인 한 사람만 접근 가능하게 하는 LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomAuthenticationForm
from .models import Post, Major1, Major2, Tag, User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View


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
        context['major1'] = Major1.objects.all()
        context['major2'] = Major2.objects.all()

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
        friends_users = User.objects.filter(username__in=friends_usernames)

        context = {'friends_users': friends_users}
        return context
    
class AddFriendView(LoginRequiredMixin, View):
    def get(self, request, friend_username, *args, **kwargs):
        friend = get_object_or_404(get_user_model(), username=friend_username)
        user_instance = self.request.user

        # 이미 친구 목록에 있는지 확인
        if friend.username not in user_instance.friends:
            # 친구를 추가하고 저장
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

        # 친구를 삭제하고 저장
        user_instance.friends = '/'.join([friend_name for friend_name in user_instance.friends.split('/') if friend_name != friend_username])
        user_instance.save()

        messages.success(self.request, f'{friend.username}님을 친구에서 삭제했습니다.')
        return redirect('/friends')
    

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


