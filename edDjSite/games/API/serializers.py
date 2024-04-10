from rest_framework import serializers
from games.models import *


class GamesSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    cat = serializers.CharField(source='cat.name')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Games
        fields = ('user', 'cat', 'title', 'slug', 'descr', 'photo', 'liked_by')
        # fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    text = serializers.CharField(read_only=True)
    class Meta:
        model = Comments
        fields = "__all__"