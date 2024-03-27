from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Count
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.http import HttpResponseNotFound, HttpResponse, JsonResponse
from .utils import *
from .models import *
from .forms import *

# Create your views here.


class GamesHome(DataMixin, ListView):
    model = Games
    template_name = 'games/index.html'
    context_object_name = 'games'

    def get_queryset(self) -> QuerySet[Any]:
        return Games.objects.filter(is_published=True).annotate(total=Count('liked_by')).order_by('-total')[:3]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(title='Главная страница')
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context


class GamesList(DataMixin, ListView):
    model = Games
    template_name = 'games/games.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(
            title='Все игры', cat_selected=1, users=self.request.user)
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context


class AuthorGames(DataMixin, ListView):
    model = Games
    template_name = 'games/author_game.html'
    context_object_name = 'games'
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return Games.objects.filter(user__username=self.kwargs['author'])

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(
            title='Игры автора ' + str(context['games'][0].user))
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context


class FavoriteList(LoginRequiredMixin, DataMixin, ListView):
    model = Games
    template_name = 'games/favorite.html'
    context_object_name = 'games'
    login_url = '/user/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self) -> QuerySet[Any]:
        favorite = Games.objects.filter(
            liked_by=self.request.user.id, is_published=True)
        return favorite

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(title='Избранные')
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context


class GameCategory(DataMixin, ListView):
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
        c_dtm = self.get_user_context(
            title=context['category'], cat_selected=context['category'].id)
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context


class AddGame(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddGameForm
    template_name = 'games/add_game.html'
    login_url = '/user/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(title='Добавление игры')
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect('games')


class ShowGame(DataMixin, FormMixin, DetailView):
    model = Games
    template_name = 'games/game.html'
    slug_url_kwarg = 'game_slug'
    context_object_name = 'game'
    form_class = AddComments

    def get_success_url(self) -> str:
        return reverse_lazy('get_game', kwargs={'game_slug': self.get_object().slug})

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(
            title=context['game'], cat_selected=context['game'].cat_id)
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form: Any) -> HttpResponse:
        self.object = form.save(commit=False)
        self.object.game = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def like_game(request):

    game_id = request.POST.get('id')
    action = request.POST.get('action')
    if game_id and action:
        try:
            game = Games.objects.get(id=game_id)
            if action == 'like':
                game.liked_by.add(request.user)
            else:
                game.liked_by.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except Games.DoesNotExist:
            pass
        return JsonResponse({'status': 'error'})


def remove_comment(request):
    comment_id = request.POST.get('id')
    if comment_id:
        try:
            comment = Comments.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({'status': 'ok'})
        except Comments.DoesNotExist:
            pass
        return JsonResponse({'status': 'error'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
