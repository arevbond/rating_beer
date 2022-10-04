from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .utils import *
from .forms import *
from .models import *


class BeerList(DataMixin, ListView):
    model = Beer
    template_name = 'ratingbeer/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Beer.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeerList, self).get_context_data()
        context['cats'] = Category.objects.all()
        return context

class UpdateRatingView(UpdateView):
    template_name = 'ratingbeer/post.html'
    success_url = reverse_lazy('home')
    form_class = AddRatingFrom

    def get_object(self, queryset=None):
        obj = Rating.objects.filter(user=self.request.user,
                                    beer_id=self.kwargs.get('post_id')).first()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Beer.objects.get(pk=self.kwargs.get('post_id'))
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.beer_id = self.kwargs.get('post_id')
        obj.save()
        return HttpResponseRedirect(reverse_lazy('home'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'ratingbeer/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    template_name = 'ratingbeer/login.html'
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class Search(ListView):
    model = Beer
    template_name = 'ratingbeer/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Beer.objects.filter(title__icontains=self.request.GET.get('q'))


class ProfileUser(ListView):
    model = Rating
    template_name = 'ratingbeer/profile.html'
    context_object_name = 'ratings'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProfileUser, self).get_context_data()
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user).order_by('-rate')
