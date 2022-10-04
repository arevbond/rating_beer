from django.urls import path
from .views import *

urlpatterns = [
    path('', BeerList.as_view(), name='home'),
    path('post/<int:post_id>/', UpdateRatingView.as_view(), name='post'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

    path('search/', Search.as_view(), name='search'),

    path('profile/', ProfileUser.as_view(), name='profile'),
]