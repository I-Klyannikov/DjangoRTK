from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.


def index(request):
    value = 10
    n1 = News('Новость 1', 'Текст 1', '08.01.24')
    n2 = News('Новость 2', 'Текст 2', '08.01.24')

    l = [n1, n2,]
    context = {'title': 'Страница главная',
               'Header1': 'Заголовок страницы',
               'value': value,
               'numbers': l,
               }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def sidebar(request):
    return render(request, 'main/sidebar.html')
