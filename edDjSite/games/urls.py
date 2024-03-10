from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('games/', games, name='games'),
    path('game/<int:id>', get_game, name='get_game'),
    path('games/<int:cat>', get_cat, name='get_cat'),
    path('add_game/', add_game, name='add_game'),
]
