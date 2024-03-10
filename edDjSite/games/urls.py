from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('games/', games, name='games'),
    path('add_game/', add_game, name='add_game'),
    path('game/<slug:game_slug>', get_game, name='get_game'),
    path('games/<slug:category_slug>', get_cat, name='get_cat'),
]
