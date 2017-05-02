# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from posts.models import Post


def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)
