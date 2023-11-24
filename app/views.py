from typing import Any
from django import http
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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
    # fields = ['username', 'email', 'password']


class List(ListView):
    model = Member
    ordering = '-pk'

class Mypage(DetailView):
    model = Member

class Friends(ListView):
    model = Member
    ordering = '-pk'

