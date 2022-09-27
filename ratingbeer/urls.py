from django.urls import path
from .views import *

urlpatterns = [
    path('', BeerList.as_view(), name='home'),
    path('post/<int:post_id>/', BeerDetail.as_view(), name='post')
]