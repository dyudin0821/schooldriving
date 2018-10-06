from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from .models import *

# Create your views here.


def index(request):
    taglines = Tagline.objects.filter(is_active=True)
    price = Price.objects.filter(is_active=True)
    branches = Branches.objects.filter(is_active=True)
    count_elements = len(branches)
    size_block = 12 / count_elements

    return render(request, 'index.html', locals())


def news(request):
    news = News.objects.filter(is_active=True)
    return render(request, 'news.html', locals())


def news_post(request, post):
    post = post
    print(post)
    full_news = News.objects.filter(is_active=True)
    return render(request, 'news_post.html', locals())
