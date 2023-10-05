
from django.urls import path
from .views import * 

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    
    # MODULO LOGIN Y REGISTRO
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),

    # MODULO DE TRABAJADORES (ADMINISTRACIÓN)
    path('listarTrabajadores/', listarTrabajadores, name='listarTrabajadores'),
    path('editarTrabajadores/<rut>/', editarTrabajadores, name='editarTrabajadores'),
    path ('eliminarTrabajadores/<rut>/', eliminarTrabajadores, name='eliminarTrabajadores'),
    path('proyectos/', proyectos, name='proyectos'),
]
