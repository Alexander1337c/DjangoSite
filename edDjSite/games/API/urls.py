from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from games.API.views import GamesViewSet, CategoryViewSet, CommentsViewSet

router = routers.SimpleRouter()
router.register(r'games', GamesViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'comments', CommentsViewSet)


urlpatterns = [

] + router.urls


