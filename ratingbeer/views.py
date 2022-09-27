from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import *


class BeerList(ListView):
    model = Beer
    template_name = 'ratingbeer/index.html'
    context_object_name = 'posts'


    def get_queryset(self):
        return Beer.objects.filter(is_published=True)


# def index(request):
#     posts = Beer.objects.filter(is_published=True)
#     context = {'posts': posts[:10],}
#
#     return render(request, 'ratingbeer/index.html', context=context)

class BeerDetail(DetailView):
    model = Beer
    template_name = 'ratingbeer/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

# def show_post(request, post_id):
#     post = get_object_or_404(Beer, pk=post_id)
#     context = {'post': post}
#
#     return render(request, 'ratingbeer/post.html', context=context)

