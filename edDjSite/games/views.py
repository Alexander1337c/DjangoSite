from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from .models import *

# Create your views here.
menu = [
    {'title': 'Игры', 'url_name': 'games'},
    {'title': 'Добавить игру', 'url_name': 'add_game'},
]


def index(request):
    context = {
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, 'games/index.html', context=context)


def games(request):
    games = Games.objects.all()
    context = {
        'title': 'Все игры',
        'menu': menu,
        'games': games,
        'cat_selected': 1
    }
    return render(request, 'games/games.html', context=context)


def get_cat(request, cat):
    if int(cat) == 1:
        games = Games.objects.all()
    elif not Games.objects.filter(cat_id=cat):
        raise Http404()
    else:
        games = Games.objects.filter(cat_id=cat)
    category = Category.objects.filter(id=cat).first()
    context = {
        'title': category,
        'menu': menu,
        'games': games,
        'cat_selected': category.id
    }
    return render(request, 'games/games.html', context=context)


def add_game(request):
    if request.method == 'POST':
        name = request.POST['name']
        descr = request.POST['descr']
        img = request.FILES.get('img')
        cat_id = request.POST['select']
        # Games.objects.create(title=name, descr=descr, photo=img, cat_id=cat_id)
        # return HttpResponseRedirect('/games')
        print(img)
    context = {
        'title': 'Добавление игры',
        'menu': menu,
        'cats': Category.objects.filter(id__gte=2).values()
    }
    return render(request, 'games/add_game.html', context=context)


def get_game(request, id):
    context = {
        'title': 'Игра ',
        'menu': menu,
        'game': Games.objects.filter(id=id)
    }

    return render(request, 'games/game.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
