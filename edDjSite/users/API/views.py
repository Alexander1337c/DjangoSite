from django.forms import model_to_dict
from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from users.API.serializers import UsersSerializer
from games.models import *


class RegisterViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny,)

    @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated], url_name='logout-user', url_path='logout-user')
    def logout_user(self, request):
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({'status':'205'})
