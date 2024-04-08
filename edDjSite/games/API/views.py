from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .permission import *
from .serializers import *
from games.models import *


class GamesAPIList(ListCreateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GamesAPIUpdate(RetrieveUpdateAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class GamesAPIDestroy(RetrieveDestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)

class CategoryViewSetsAPI(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

