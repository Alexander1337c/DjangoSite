from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddGameForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Выберите категорию'

    class Meta:
        model = Games
        fields = ['cat', 'title', 'slug', 'descr', 'photo']
        widgets = {
            'cat': forms.Select(attrs={'class': 'cat-name', 'placeholder': 'Категории'}),
            'title': forms.TextInput(attrs={'placeholder': 'Название игры'}),
            'slug': forms.TextInput(attrs={'placeholder': 'URL для игры "mortal-combat" '})
        }
    # def clean_slug(self):
    #     slug = self.cleaned_data['slug']
    #     if slug:
    #         raise ValidationError('Такой слаг уже существует')
    #     return slug


class AddComments(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)
        widgets = {'text': forms.Textarea(
            attrs={'class': 'comment-field', 'placeholder': 'Введите текст комментария'})}
