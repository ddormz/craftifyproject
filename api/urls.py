from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('listarProyectos/', listarProyectos, name='listarProyectos'),
    path('cotizaciones/', cotizaciones, name='cotizaciones'),
    path('listarTrabajadores/', listarTrabajadores, name='listarTrabajadores'),
    path('listarProductos/', listarProductos, name='listarProductos'),
    path('listarCategorias/', listarCategorias, name='listarCategorias'),
    path('listarSubCategorias/', listarSubCategorias, name='listarSubCategorias'),
    path('listarMarcas/', listarMarcas, name='listarMarcas'),
    path('listarEquipos/', listarEquipos, name='listarEquipos'),
    path('listarAvances/', listarAvances, name='listarAvances'),
    path('listarVariantes/', listarVariantes, name='listarVariantes'),
    path('listarAsignaciones/', listarAsignaciones, name='listarAsignaciones'),
    path('listarStatus/', listarStatus, name='listarStatus'),
    path('detalleCotizaciones/', detalleCotizaciones, name='detalleCotizaciones'),
]



