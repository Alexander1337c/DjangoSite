from django.urls import path

from .views import *

urlpatterns = [
    path('', GamesHome.as_view(), name='home'),
    path('games/', GamesList.as_view(), name='games'),
    path('add_game/', AddGame.as_view(), name='add_game'),
    path('games/game/<slug:game_slug>', ShowGame.as_view(), name='get_game'),
    path('games/<slug:category_slug>', GameCategory.as_view(), name='get_cat'),
]
