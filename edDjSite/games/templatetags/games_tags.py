from django import template
from django.http import Http404
from games.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_games():
    return Games.objects.all()


@register.inclusion_tag('games/categories.html')
def show_categories(cat_selected=1):
    ctg = Category.objects.all()
    return {"ctg": ctg, 'cat_selected': cat_selected}


@register.inclusion_tag('games/show_games.html')
def show_games(cat_games=1, user=None):
    if cat_games and cat_games == 1:
        games = Games.objects.filter(is_published=True).select_related('cat', 'user').prefetch_related('liked_by', 'comments_games')
    elif not Games.objects.filter(cat_id=cat_games):
        raise Http404()
    else:
        games = Games.objects.filter(is_published=True, cat_id=cat_games ).select_related('cat', 'user').prefetch_related('liked_by', 'comments_games')
    return {"games": games, "user": user}
