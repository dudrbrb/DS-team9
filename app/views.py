from django.shortcuts import render

from .models import Major1, Major2, Tag, Member

# Create your views here.

def main(request):
    return render(
        request,
        'main.html',

    )

def join():
    return

def login():
    return

def list():
    return

def mypage():
    return

def myfriends():
    return

def message():
    return
