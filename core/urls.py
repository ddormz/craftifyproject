
from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]
