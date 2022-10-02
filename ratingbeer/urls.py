from django.urls import path
from .views import *

urlpatterns = [
    path('', BeerList.as_view(), name='home'),
    path('post/<int:post_id>/', BeerDetail.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')

]