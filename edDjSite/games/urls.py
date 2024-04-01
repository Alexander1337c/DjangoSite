from django.urls import path

from .views import *

urlpatterns = [
    path('', GamesHome.as_view(), name='home'),
    path('search/', GamesHome.as_view(), name='search'),
    path('games/', GamesList.as_view(), name='games'),
    path('add_game/', AddGame.as_view(), name='add_game'),
    path('favorite/', FavoriteList.as_view(), name='favorite'),
    path('like', like_game, name='like_game'),
    path('dynamic_search', dynamic_search, name='d_search'),
    path('remove', remove_comment, name='remove_comment'),
    path('games/game/<slug:game_slug>', ShowGame.as_view(), name='get_game'),
    path('games/<slug:category_slug>', GameCategory.as_view(), name='get_cat'),
    path('author_game/<str:author>', AuthorGames.as_view(), name='author_game'),

]
