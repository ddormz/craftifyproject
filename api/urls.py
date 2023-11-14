from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('apiproyectos/', apiproyectos, name='apiproyectos'),
    path('apicotizaciones/', apicotizaciones, name='apicotizaciones'),
    path('apitrabajadores/', apitrabajadores, name='apitrabajadores'),
    path('apiproductos/', apiproductos, name='apiproductos'),
    path('apiveravances/', apiveravances, name='apiveravances'),
    path('cotizaciones/pdf/<id_cotizacion>/', cotizaciones_pdf_api, name='cotizaciones-pdf-api'),
    path('login/', LoginView.as_view(), name='login'),
    path('apitareas/', apitareas, name='apitareas'),
    path('apiagregaravances/', apiagregaravances, name='apiagregaravances'),
    path('apieditaravances/<int:pk>/', apieditaravances, name='apieditaravances'),
]



