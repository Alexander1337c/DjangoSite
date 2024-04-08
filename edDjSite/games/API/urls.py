from django.urls import include, path, re_path
from rest_framework import routers
from games.API.views import *

# router = routers.SimpleRouter()
# router.register(r'games', GamesViewSetsAPI)
# router.register(r'category', CategoryViewSetsAPI)

urlpatterns = [
    path('games/', GamesAPIList.as_view()),
    path('games/<int:pk>/', GamesAPIUpdate.as_view()),
    path('gamesdelete/<int:pk>/', GamesAPIDestroy.as_view()),
    path('category/', CategoryViewSetsAPI.as_view()),
    path('categorydelete/<int:pk>', CategoryViewSetsAPI.as_view()),
    path('drf-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
