from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout

from .utils import *
from .forms import *
from .models import *


class BeerList(DataMixin, ListView):
    model = Beer
    template_name = 'ratingbeer/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Beer.objects.filter(is_published=True)


class BeerDetail(DetailView):
    model = Beer
    template_name = 'ratingbeer/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'ratingbeer/register.html'
    success_url = reverse_lazy('home') # change to login

class LoginUser(LoginView):
    template_name = 'ratingbeer/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
