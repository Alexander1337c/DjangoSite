from django.db import models
from django.urls import reverse

# Create your models here.


class Games(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    descr = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='imgs/', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('get_game', kwargs={'game_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('get_cat', kwargs={'category_slug': self.slug})
