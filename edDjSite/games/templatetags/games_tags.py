from django import template
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
