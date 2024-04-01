from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='user_login'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
]
