from django.contrib import admin

# Register your models here.
from .models import *


class GamesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Games, GamesAdmin)
admin.site.register(Category, CategoryAdmin)
