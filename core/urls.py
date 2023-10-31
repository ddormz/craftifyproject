
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import * 

urlpatterns = [
    path('', home, name='home'),
    
    # MODULO LOGIN Y REGISTRO
    path('logout/', exit, name='exit'),
    #path('register/', register, name='register'),

    # MODULO DE TRABAJADORES (ADMINISTRACIÓN)
    path('listarTrabajadores/', listarTrabajadores, name='listarTrabajadores'),
    path('editarTrabajadores/<rut>/', editarTrabajadores, name='editarTrabajadores'),
    path ('eliminarTrabajadores/<rut>/', eliminarTrabajadores, name='eliminarTrabajadores'),

    # MODULO DE PROYECTOS
    path('verproyectos/', verproyectos, name='verproyectos'),
    path('agregarProyecto/', agregarProyecto, name='agregarProyecto'),
    path('editarProyecto/<id_proyecto>/', editarProyecto, name='editarProyecto'),
    path('eliminarProyecto/<id_proyecto>/', eliminarProyecto, name='eliminarProyecto'),

    # MODULO DE AVANCES
    path('avances', avances, name='avances'),
    path('statusProyectos', statusProyectos, name='statusProyectos'),
    path('agregarAvances', agregarAvances, name='agregarAvances'),

    # MODULO DE COTIZACIONES
    path('listarCotizaciones', CotListView.as_view(), name='listarCotizaciones'),
    path('agregarCotizaciones', CotView.as_view(), name='agregarCotizaciones'),
    path('eliminarCotizaciones/<id_cotizacion>/', eliminarCotizaciones, name='eliminarCotizaciones'),
    path('editarCotizaciones/<int:pk>/', CotUpdateView.as_view(), name='editarCotizaciones'),

    # MODULO DE CLIENTES
    path('listarClientes', listarClientes, name='listarClientes'),
    path('agregarClientes', agregarClientes, name='agregarClientes'),

    # MODULO DE PRODUCTOS
    path('listarProductos', listarProductos, name='listarProductos'),
    path('agregarProductos', agregarProductos, name='agregarProductos'),
    path('listarCatySubcat', listarCatySubcat, name='listarCatySubcat'),
    path('agregarCatySubcat', agregarCatySubcat, name='agregarCatySubcat'),

    # MODULO DE EQUIPOS 

    path('listarEquipos', listarEquipos, name='listarEquipos'),
    path('agregarEquipos', agregarEquipos, name='agregarEquipos'),

    # MODULO ASIGNACIONES

    path('listarAsignaciones', listarAsignaciones, name='listarAsignaciones'),
    path('agregarAsignaciones', agregarAsignaciones, name='agregarAsignaciones')
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
