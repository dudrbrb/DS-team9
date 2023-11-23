from django.shortcuts import render

from .models import Major1, Major2, Tag, Member

# Create your views here.

def main(request):
    return render(
        request,
        'main.html',
<<<<<<< HEAD

=======
>>>>>>> 4a11cbcf5cc58b7ae73819bf6eb386bcb488cb36
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


