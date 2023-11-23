from django.shortcuts import render

from .models import Major1, Major2, Tag, Member

# Create your views here.

def main(request):
    return render(
        request,
        'main.html',
    )

def join(request):
    return render(
        request,
        'join.html',
    )

def login(request):
    return render(
        request,
        'login.html',
    )

def list(request):
    return render(
        request,
        'list.html',
    )

def mypage(request):
    return render(
        request,
        'mypage.html',
    )

def myfriends(request):
    return render(
        request,
            'friend.html',
    )


