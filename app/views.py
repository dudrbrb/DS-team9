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
    return

def login(request):
    return

def list(request):
    return

def mypage(request):
    return

def myfriends(request):
    return

def message(request):

    return
