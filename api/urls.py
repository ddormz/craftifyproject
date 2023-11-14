from django.urls import path

from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [

    path('apiproyectos/', apiproyectos, name='apiproyectos'),
    path('apicotizaciones/', apicotizaciones, name='apicotizaciones'),
    path('apidetallecotizaciones/', apidetallecotizaciones, name='apidetallecotizaciones'),
    path('apitrabajadores/', apitrabajadores, name='apitrabajadores'),
    path('apiproductos/', apiproductos, name='apiproductos'),
    path('apicategorias/', apicategorias, name='apicategorias'),
    path('apisubcategorias/', apisubcategorias, name='apisubcategorias'),
    path('apiveravances/', apiveravances, name='apiveravances'),
    path('apistatus', apistatus, name='apistatus'),
    path('apiclientes', apiclientes, name='apiclientes'),
    path('cotizaciones/pdf/<id_cotizacion>/', cotizaciones_pdf_api, name='cotizaciones-pdf-api'),



]



