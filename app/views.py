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


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # 인스턴스를 바로 저장하지 않음
            user.tag.set(form.cleaned_data['tag'])
            user.prof_image = form.cleaned_data['prof_image']
            user.back_image = form.cleaned_data['back_image']
            user.save()

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
    def get_context_data(self, **kwargs):
        context = super(Friends, self).get_context_data()
      
        return context


