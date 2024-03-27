from typing import Any
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from games.utils import DataMixin
from .forms import *

# Create your views here.

class LoginUser(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(title='Авторизация')
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context
    
    def get_success_url(self) -> str:
        return reverse_lazy('home')



class RegisterUser(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/registration.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_dtm = self.get_user_context(title='Регистрация')
        context = dict(list(context.items()) + list(c_dtm.items()))
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')



def logout_user(request):
    logout(request)
    return redirect('user_login')