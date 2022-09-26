from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def index(request):
    posts = Beer.objects.filter(is_published=True)
    context = {'posts': posts[:10],
               }

    return render(request, 'ratingbeer/index.html', context=context)

def show_post(request, post_id):
    post = get_object_or_404(Beer, pk=post_id)
    context = {'post': post}

    return render(request, 'ratingbeer/post.html', context=context)

