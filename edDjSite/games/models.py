from typing import Any
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
# Create your models here.


class Games(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    descr = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='imgs/', verbose_name='Фото')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='Категория')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    liked_by = models.ManyToManyField(
        User, related_name='liked_games', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_game', kwargs={'game_slug': self.slug})



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('get_cat', kwargs={'category_slug': self.slug})


class Comments(models.Model):
    game = models.ForeignKey(
        Games, related_name='comments_games', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Игра')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Автор')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    text = models.TextField(verbose_name='Текст комментария')
    status = models.BooleanField(verbose_name='Видимость', default=True)
