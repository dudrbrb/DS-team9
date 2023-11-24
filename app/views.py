from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView,TemplateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   # 로그인 한 사람만 접근 가능하게 하는 LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from .models import Major1, Major2, Tag, Member

# Create your views here.

class Main(ListView):
    model = Member
    ordering = '-pk'
    template_name = 'main.html'


    def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data()
        # context['categories'] = Category.objects.all()
        # context['no_category_post_count'] = Member.objects.filter(category=None).count()

        return context

class Join(generic.CreateView):
    model = Member
    template_name = 'join.html'
    fields = [
        'member_name', 
        'member_id', 
        'member_password',
        'member_birthday',
        'member_studentNumber',
        'member_major_1',
        'member_major_2',
        'member_hash',
        'prof_image',
        'back_image',
        ]


class List(ListView):
    model = Member
    ordering = '-pk'
    template_name = 'list.html'


class Mypage(LoginRequiredMixin, UpdateView):
    model = Member
    fields = [
        'member_password',
        'member_birthday',
        'member_major_1',
        'member_major_2',
        'member_hash',
        'prof_image',
        'back_image',
        ]
    template_name = 'mypage.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:   
            return super(Mypage, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class Friends(ListView):
    model = Member
    ordering = '-pk'
    template_name = 'friends.html'
