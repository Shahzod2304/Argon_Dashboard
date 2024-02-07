from django.urls import path 
from .views import *

urlpatterns=[
    path('', Home, name='home'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('documentation/', Documentation, name='documentation'),
    path('profile/',Profile, name='profile'),
    path('sign-in/', Sign_In, name='sign_in'),
    path('sign-up/', Sign_Up, name='sign_up'),
    path('tables/', Tables, name='tables'),
]