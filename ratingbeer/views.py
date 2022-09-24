from django.shortcuts import render
from .models import *

def index(request):
    posts = Beer.objects.all()
    return render(request, 'ratingbeer/index.html', {'posts': posts})

