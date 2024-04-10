from django.forms import model_to_dict
from rest_framework import mixins, serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from .permission import *
from .serializers import *
from games.models import *


class GameAPIListPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 10000


class GamesViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    pagination_class = GameAPIListPagination

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        user = User.objects.filter(pk=request.data.get('user_id')).first()
        game = self.get_object()
        liked = user in game.liked_by.all()
        if liked:
            game.liked_by.remove(user)
        else:
            game.liked_by.add(user)
        return Response({"like": not liked})

    @action(methods=['POST', 'DELETE'], detail=True, permission_classes=[IsAuthenticated])
    def comment(self, request, pk=None):
        if request.method == 'POST':
            serializer = CommentsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"comment": "add comment"})
        elif request.method == 'DELETE':
            comment_id = self.request.data.get('comment_id')
            comment = Comments.objects.filter(pk=comment_id).first()
            if not Comments.objects.filter(pk=comment_id):
                return Response({'error': 'Comment does not exists'})
            if request.user == comment.author:
                Comments.objects.get(pk=comment_id).delete()
                return Response({"status": "remove comment"})
            return Response({'error': 'you do not access'})


class CommentsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
    @action(methods=['GET'], detail=False, url_path='comments-game')
    def comments_game(self, requset, *args, **kwargs):
        print(self.action)
        queryset = Comments.objects.filter(game=self.request.data.get('game_id'))
        return Response({'comments': CommentsSerializer(queryset, many=True).data})
    
    
class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
