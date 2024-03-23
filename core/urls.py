
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import * 

urlpatterns = [
    
    path('', HomeDashboard.as_view(), name='home'),
    
    # MODULO LOGIN Y REGISTRO
    path('logout/', exit, name='exit'),
    #path('register/', register, name='register'),
    path('reset/', ResetPasswordView.as_view(), name='reset'),
    path('change/password/<str:token>/', ChangePasswordView.as_view(), name='change_password'),



    # MODULO DE TRABAJADORES (ADMINISTRACIÓN)
    path('listarTrabajadores/', listarTrabajadores, name='listarTrabajadores'),
    path('editarTrabajadores/<rut>/', editarTrabajadores, name='editarTrabajadores'),
    path ('eliminarTrabajadores/<rut>/', eliminarTrabajadores, name='eliminarTrabajadores'),

    # MODULO DE PROYECTOS
    path('verproyectos/', verproyectos, name='verproyectos'),
    path('agregarProyecto/', agregarProyecto, name='agregarProyecto'),
    path('editarProyecto/<id_proyecto>/', editarProyecto, name='editarProyecto'),
    path('eliminarProyecto/<id_proyecto>/', eliminarProyecto, name='eliminarProyecto'),
    path('categoriaproyecto/', categoriaProyectos, name='categoriaproyecto'),
    path('eliminarcategoria/<id_categoria>/', eliminarCategoria, name='eliminarCategoria'),
    path('editarCategoria/<id_categoria>/', editarCategoria, name='editarcategoria'),
    path('statusp', StatusProyectos, name='statusProyectos'),
    path('metodopago/', metodopagos, name='metodopago'),
    path('eliminarmetodo/<id_metodopago>/', eliminarMetodo, name='eliminarMetodo'),
    path('editarmetodo/<id_metodopago>/', editarMetodo, name='editarmetodo'),
    path('ediStatus/<id_status_p>/', editStatus, name='editStatus'), 
    path('elimStat/<id_status_p>/', elimStatus, name='elimStatus'),
    path('formapago/', formapagos, name='formapago'),
    path('eliminarFormaPago/<id_formapago>/', eliminarFormaPago, name='eliminarFormaPago'),
    path('editarFormaPago/<id_formapago>/', editarFormaPago, name='editarFormaPago'),

    # MODULO DE AVANCES
    path('avances', ListarAvances.as_view(), name='avances'),

    path('agregarAvances', agregarAvances, name='agregarAvances'),
    path('editarAvance/<avance_id>/', editarAvances, name='editarAvances'),
    path('eliminarAvance/<avance_id>/', eliminarAvances, name='eliminarAvance'),
    path('avanceproyecto/<proyecto_id_proyecto>/', listarAvancesporIdProyecto.as_view(), name='avanceproyecto'),
    path('elimavanceproyecto/<avance_id>/', eliminarAvancesPorProyecto, name='elimavanceproyecto'),
    path('editavanceproyecto/<avance_id>/', editarAvancesPorProyecto, name='editavanceproyecto'),

    # MODULO DE COTIZACIONES
    path('listarCotizaciones', CotListView.as_view(), name='listarCotizaciones'),
    path('agregarCotizaciones', CotView.as_view(), name='agregarCotizaciones'),
    path('eliminarCotizaciones/<id_cotizacion>/', eliminarCotizaciones, name='eliminarCotizaciones'),
    path('editarCotizaciones/<int:pk>/', CotUpdateView.as_view(), name='editarCotizaciones'),
    path('cotpdf/<int:pk>/', CotizacionesPDF.as_view(), name='cotpdf'),
    path('statuscot', statuscotizaciones, name='statuscot'),
    path('editstatuscot/<id_estado>/', editStatusCotizaciones, name='editstatuscot'),
    path('elimstatuscot/<id_estado>/', eliminarstatuscotizaciones, name='elimstatuscot'),

    # MODULO DE CLIENTES
    path('listarClientes', listarClientes, name='listarClientes'),
    path('agregarClientes', agregarClientes, name='agregarClientes'),
    path('eliminarClientes/<rut_cliente>/', eliminarClientes, name='eliminarClientes'),
    path('editarClientes/<rut_cliente>/', editarClientes, name='editarClientes'),

    # MODULO DE PRODUCTOS
    path('listarProductos', ProductosListView.as_view(), name='listarProductos'),
    path('agregarProductos', agregarProductos, name='agregarProductos'),
    path('agregarCatySubcat', agregarCatySubcat, name='agregarCatySubcat'),
    path('eliminarProductos/<id_producto>/', eliminarProductos, name='eliminarProductos'),
    path('editarProductos/<id_producto>/', editarProductos, name='editarProductos'),

    # CATEGORIAS PRODUCTOS
    path('catproductos', categoriaProd, name='catproductos'),
    path('eliminarCat/<id_categoria>/', eliCat, name='eliminarCat'),
    path('editarCat/<id_categoria>/', editarCat, name='editarCat'),

    #SUBCATEGORIA PRODUCTOS

    path('subcatproductos', subCat, name='subcatproductos'),
    path('eliSubcat/<id_subcategoria>/', eliSubCat, name='eliSubcat'),
    path('editaSubcat/<id_subcategoria>/', editarSubCat, name='editaSubcat'),

    # MARCA PRODUCTOS
    path('marcaproductos', marcaProd, name='marcaproductos'),
    path('eliMarca/<id_marca>/', eliMarca, name='eliMarca'),
    path('editaMarca/<id_marca>/', editarMarca, name='editaMarca'),

    # MODULO TODAS (LISTAR CAT, SUB, MARCAS)

    path('todas', catSubMar, name='todas'),

    
    # MODULO DE EQUIPOS 

    path('listarEquipos', EquipoListView.as_view(), name='listarEquipos'),
    path('agregarEquipos', Equipo.as_view(), name='agregarEquipos'),
    path('eliminarEquipo/<id_equipo>/', EliminarEquipo, name='eliminarEquipos'),
    path('editarEquipo/<int:pk>/', EquipoEdit.as_view(), name='editarEquipo'),

    # MODULO TAREAS
    path('statusTareas', statusTarea, name='statusTareas'),
    path('eliStatusTarea/<id_status_tarea>/', eliStatus, name='eliminarStatusTarea'),
    path('ediStatusTarea/<id_status_tarea>/', editarStatus, name='editaStatusTarea'),
    ##
    path('listarTareas', TareasListView.as_view(), name='listarTareas'),
    path('agregarTareas', agregarTareas, name='agregarTareas'),
    path('eliminarTareas/<tarea_id>/', eliminarTareas, name='eliminarTareas'),
    path('editarTareas/<tarea_id>/', editarTareas, name='editarTareas'),

    

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
