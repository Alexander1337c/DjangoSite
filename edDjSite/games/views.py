from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.http import HttpResponseNotFound
from .models import *
from .forms import *

# Create your views here.
menu = [
    {'title': 'Игры', 'url_name': 'games'},
    {'title': 'Добавить игру', 'url_name': 'add_game'},
]


class GamesHome(TemplateView):
    template_name = 'games/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


class GamesList(ListView):
    model = Games
    template_name = 'games/games.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = 1
        context['title'] = 'Все игры'
        context['menu'] = menu
        return context


class GameCategory(ListView):
    model = Category
    template_name = 'games/games.html'
    context_object_name = 'category'
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        category = Category.objects.filter(
            slug=self.kwargs['category_slug']).first()
        return category

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cat_selected'] = context['category'].id
        context['title'] = context['category']
        context['menu'] = menu
        return context


class AddGame(CreateView):
    form_class = AddGameForm
    template_name = 'games/add_game.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление игры'
        context['menu'] = menu
        return context


class ShowGame(DetailView):
    model = Games
    template_name = 'games/game.html'
    slug_url_kwarg = 'game_slug'
    context_object_name = 'game'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = context['game'].title
        context['menu'] = menu
        context['cat_selected'] = context['game'].cat_id
        return context


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
