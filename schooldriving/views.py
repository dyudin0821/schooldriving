from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import loader, Context
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import *


# Create your views here.


def index(request):
    taglines = Tagline.objects.filter(is_active=True)
    studying_program = Price.objects.filter(is_active=True)
    branches = Branches.objects.filter(is_active=True)
    information = Information.objects.filter(is_active=True)
    return render(request, 'index.html', locals())


def teachers(request):
    teachers = Teachers.objects.filter(is_active=True)
    return render(request, 'teachers.html', locals())


def classes(request):
    branches = Branches.objects.filter(is_active=True)
    return render(request, 'classes.html', locals())


def form_record(request, branch):
    branches = Branches.objects.get(url=branch)
    category = Price.objects.all()
    price = Price.objects.filter(is_active=True)
    branch_name = branches.name
    return render(request, 'record_courses.html', locals())


def add_order(request):
    if request.POST:
        name = request.POST['full_name']
        email = request.POST['email']
        phone = request.POST['phone']
        branch = request.POST['branch']
        cat = request.POST['category']
        category = Price.objects.get(name=cat)
        filial = Branches.objects.get(name=branch)
        contact = Contacts.objects.get(id=filial.id)
        order = Orders(name=name, email=email, phone=phone, branch=filial, category=category)
        order.save()
        sbj = 'Внимание! Новая заявка от %s; Номер телефона: %s' % (name, phone)
        msg = "Новая заявка с сайта\n" \
              "%s желает записаться на %s в филиале %s\n" \
              "------- Данные клиента -------\n" \
              "Имя: %s\n" \
              "Телефон: %s\n" \
              "E-mail: %s\n" \
              % (name, cat, branch, name, phone, email)
        send_mail(sbj, msg, settings.EMAIL_HOST_USER, [contact.admin_email])
        return JsonResponse({'location': '/'})
    else:
        get = request.GET
        print(get)
        return HttpResponse('Error')


def news(request, page_number=1):
    # news_list = News.objects.filter(is_active=True).order_by('-data_news')
    news_list = News.objects.filter(is_active=True).order_by('-data_news')
    for n in news_list:
        print(n.data_news)
    current_page = Paginator(news_list, 3)
    pages = current_page.page(page_number)
    return render(request, 'news.html', locals())


def news_post(request, post):
    post = post
    full_news = News.objects.filter(is_active=True)
    return render(request, 'news_post.html', locals())


def get_confidential(request):
    return render(request, 'confidential.html', locals())


def contacts(request):
    about = About.objects.filter(id=1, is_active=True)
    return render(request, 'contacts.html', locals())

