
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

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
    path('agregarProyecto/', agregarProyecto, name='agregarProyecto'),
    path('editarProyecto/<id_proyecto>/', editarProyecto, name='editarProyecto'),
    path('eliminarProyecto/<id_proyecto>/', eliminarProyecto, name='eliminarProyecto'),
    path('avances', avances, name='avances'),
    path('statusProyectos', statusProyectos, name='statusProyectos'),
    path('listarCotizaciones', listarCotizaciones, name='listarCotizaciones'),
    path('agregarCotizaciones', agregarCotizaciones, name='agregarCotizaciones'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
