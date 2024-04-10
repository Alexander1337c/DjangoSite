from django.urls import include, path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework import routers
from users.API.views import RegisterViewSet

router = routers.SimpleRouter()
router.register(r'auth-user', RegisterViewSet )

urlpatterns = [

    # Авторизация с помощью jwt библиотеки
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

] + router.urls
