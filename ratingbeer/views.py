from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    posts = Beer.objects.all()
    context = {'posts': posts[:10],
               }

    return render(request, 'ratingbeer/index.html', context=context)

def show_post(requset, post_id):
    return HttpResponse(f'Пост с id: {post_id}')

