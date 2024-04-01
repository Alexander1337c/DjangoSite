from .models import *
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


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


def q_search(terms):

    # vector = SearchVector("title", "descr")
    # query = SearchQuery(terms)

    # print(query)
    # return Games.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
    keywords: list = [word for word in terms.split() if len(terms) >= 2]
    q_objects = Q()
    for token in keywords:
        q_objects |= Q(descr__icontains=token)
        q_objects |= Q(title__icontains=token)

    return Games.objects.filter(q_objects)
