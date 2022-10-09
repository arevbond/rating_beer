from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', BeerList.as_view(), name='home'),
    path('post/<int:post_id>/', UpdateRatingView.as_view(), name='post'),
    path('category/<slug:cat_slug>', CategoriesList.as_view(), name='category'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

    path('search/', Search.as_view(), name='search'),

    path('profile/', ProfileUser.as_view(), name='profile'),
    path('profile/avatar/', UserProfilePictureCreate.as_view(), name='avatar'),

    path('about/', about, name='about')
]

