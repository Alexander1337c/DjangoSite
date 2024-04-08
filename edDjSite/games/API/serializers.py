from rest_framework import serializers
from games.models import *


class GamesSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    cat = serializers.CharField(source='cat.name')
    # user = serializers.CharField(source='user.username')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Games
        fields = ('user', 'cat', 'title', 'slug', 'descr', 'photo')
        # fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

