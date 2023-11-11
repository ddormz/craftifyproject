
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import * 

urlpatterns = [
    
    path('', HomeDashboard.as_view(), name='home'),
    
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
    path('agregarCategoriaProyecto/', agregarCategoriaProyecto, name='agregarCategoriaProyecto'),

    # MODULO DE AVANCES
    path('avances', ListarAvances.as_view(), name='avances'),
    path('statusProyectos', statusProyectos, name='statusProyectos'),
    path('agregarAvances', agregarAvances, name='agregarAvances'),
    path('editarAvance/<avance_id>/', editarAvances, name='editarAvances'),
    path('eliminarAvance/<avance_id>/', eliminarAvances, name='eliminarAvance'),

    # MODULO DE COTIZACIONES
    path('listarCotizaciones', CotListView.as_view(), name='listarCotizaciones'),
    path('agregarCotizaciones', CotView.as_view(), name='agregarCotizaciones'),
    path('eliminarCotizaciones/<id_cotizacion>/', eliminarCotizaciones, name='eliminarCotizaciones'),
    path('editarCotizaciones/<int:pk>/', CotUpdateView.as_view(), name='editarCotizaciones'),
    path('cotpdf/<int:pk>/', CotizacionesPDF.as_view(), name='cotpdf'),

    # MODULO DE CLIENTES
    path('listarClientes', listarClientes, name='listarClientes'),
    path('agregarClientes', agregarClientes, name='agregarClientes'),

    # MODULO DE PRODUCTOS
    path('listarProductos', ProductosListView.as_view(), name='listarProductos'),
    path('agregarProductos', agregarProductos, name='agregarProductos'),
    path('listarCatySubcat', listarCatySubcat, name='listarCatySubcat'),
    path('agregarCatySubcat', agregarCatySubcat, name='agregarCatySubcat'),
    path('eliminarProductos/<id_producto>/', eliminarProductos, name='eliminarProductos'),
    path('editarProductos/<id_producto>/', editarProductos, name='editarProductos'),

    # MODULO DE EQUIPOS 

    path('listarEquipos', EquipoListView.as_view(), name='listarEquipos'),
    path('agregarEquipos', Equipo.as_view(), name='agregarEquipos'),
    path('eliminarEquipo/<id_equipo>/', EliminarEquipo, name='eliminarEquipos'),
    path('editarEquipo/<int:pk>/', EquipoEdit.as_view(), name='editarEquipo'),

    # MODULO ASIGNACIONES

    path('listarTareas', TareasListView.as_view(), name='listarTareas'),
    path('agregarTareas', agregarTareas, name='agregarTareas'),
    path('eliminarTareas/<tarea_id>/', eliminarTareas, name='eliminarTareas'),
    path('editarTareas/<tarea_id>/', editarTareas, name='editarTareas'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
