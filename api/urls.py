from django.urls import path

from .views import *



urlpatterns = [

    path('listarProyectos/', listarProyectos, name='listarProyectos'),

]



