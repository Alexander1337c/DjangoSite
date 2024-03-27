from .models import *


menu = [
    {'title': 'Игры', 'url_name': 'games'},
    {'title': 'Добавить игру', 'url_name': 'add_game'},
    {'title': 'Избранные', 'url_name': 'favorite'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['ctg'] = cats
        if not self.request.user.is_authenticated:
            list_menu = []
            list_menu.append(menu[0])
            context['menu'] = list_menu
        return context
