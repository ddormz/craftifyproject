import json
from django.http import FileResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, View, TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime
from django.db.models.functions import Coalesce
from django.db.models import Sum

# Create your views here.


class HomeDashboard(TemplateView):
    template_name = 'core/home.html'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_graph_data(self):
        try:
            data = []
            year = datetime.now().year
            for m in range(1, 13):
                cotizaciones = Cotizaciones.objects.filter(fecha_cotizacion__year=year, fecha_cotizacion__month=m).count()
                data.append(cotizaciones)
        except:
            pass    
        return data
    
    def get_graph_data_proyectos(self):
        try:
            data = []
            year = datetime.now().year
            for m in range(1, 13):
                proyectos = Proyecto.objects.filter(fecha__year=year, fecha__month=m).count()
                data.append(proyectos)

        except:
            data = [0,0,0,0,0,0,0,0,0,0,0,0]
        return data


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Dashboard'
        context['entity'] = 'Dashboard'
        context['get_graph_data'] = json.dumps(self.get_graph_data())
        context['get_graph_data_proyectos'] = json.dumps(self.get_graph_data_proyectos())
        return context

def exit(request):
    logout(request)
    return redirect('login')

@login_required

# MODULO USUARIOS 

def listarTrabajadores(request):
    users = User.objects.all()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = form.errors.as_json()
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    
    form = CustomUserCreationForm()
    
    contexto = {'users': users, 'form': form}
    return render(request, 'trabajadores/listarTrabajadores.html', contexto)
@login_required
def editarTrabajadores(request, rut):
    user = User.objects.get(rut=rut)
    data = {
        'editTrabajador': editarTrabajadorForm(instance=user)
    }
    if request.method == 'POST':
        formulario = editarTrabajadorForm(data=request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarTrabajadores')
        else:
            data['form'] = formulario

    return render(request, 'trabajadores/editarTrabajador.html', data)
@login_required
def eliminarTrabajadores(request, rut):
    user = User.objects.get(rut=rut)
    user.delete()
    return redirect('listarTrabajadores')

# MODULO PROYECTOS

@login_required
def verproyectos(request):
    proyectos = Proyecto.objects.all()

    for proyecto in proyectos:
        fecha_creacion = proyecto.fecha
        plazo_entrega = proyecto.plazo_entrega

        if fecha_creacion and plazo_entrega:
            fecha_creacion = datetime.combine(fecha_creacion, datetime.min.time())
            plazo_entrega = datetime.combine(plazo_entrega, datetime.min.time())

            tiempo_restante = (plazo_entrega - fecha_creacion).days

            # Asegurarse de que el tiempo restante no sea negativo
            tiempo_restante = max(tiempo_restante, 0)

            proyecto.tiempo_restante = tiempo_restante

    contexto = {'proyectos': proyectos}
    return render(request, 'proyectos/proyectos.html', contexto)
@login_required
def agregarProyecto(request):
    data = {
        'AggForm': AgregarProyectoForm()
    }
    if request.method == 'POST':
        formulario = AgregarProyectoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('verproyectos')
        else:
            data['AggForm'] = formulario
    
    return render(request, 'proyectos/agregarProyecto.html', data)

def editarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id_proyecto=id_proyecto)
    data = {
        'form': ProyectoForm(instance=proyecto)
    }
    if request.method == 'POST':
        formulario = ProyectoForm(data=request.POST, instance=proyecto)
        if formulario.is_valid():
            formulario.save()
            return redirect('verproyectos')
        else:
            data['form'] = formulario
    
    return render(request, 'proyectos/editarProyecto.html', data)

def eliminarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id_proyecto=id_proyecto)
    proyecto.delete()
    return redirect('verproyectos')

def StatusProyectos(request):
    status = StatusProyecto.objects.all()
    
    if request.method == 'POST':
        form = StatusProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = form.errors.as_json()
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    
    form = StatusProyectoForm()
    
    contexto = {'status': status, 'form': form}
    return render(request, 'proyectos/statusProyectos.html', contexto)

def elimStatus(request, id_status_p):
    status = StatusProyecto.objects.get(id_status_p=id_status_p)
    status.delete()
    return redirect('statusProyectos')

def editStatus(request, id_status_p):
    status = StatusProyecto.objects.get(id_status_p=id_status_p)
    data = {
        'form': StatusProyectoForm(instance=status)
    }
    if request.method == 'POST':
        formulario = StatusProyectoForm(data=request.POST, instance=status)
        if formulario.is_valid():
            formulario.save()
            return redirect('statusProyectos')
        else:
            data['form'] = formulario
    
    return render(request, 'proyectos/editarStatus.html', data)


def metodopagos(request):
    metodos = MetodoPago.objects.all()
    
    if request.method == 'POST':
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = form.errors.as_json()
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    
    form = MetodoPagoForm()
    
    contexto = {'metodos': metodos, 'form': form}
    return render(request, 'cotizaciones/metodoPago.html', contexto)

def eliminarMetodo(request, id_metodopago):
    metodo = MetodoPago.objects.get(id_metodopago=id_metodopago)
    metodo.delete()
    return redirect('metodopago')

def editarMetodo(request, id_metodopago):
    metodo = MetodoPago.objects.get(id_metodopago=id_metodopago)
    data = {
        'form': MetodoPagoForm(instance=metodo)
    }
    if request.method == 'POST':
        formulario = MetodoPagoForm(data=request.POST, instance=metodo)
        if formulario.is_valid():
            formulario.save()
            return redirect('metodopago')
        else:
            data['form'] = formulario
    
    return render(request, 'cotizaciones/editarMetodo.html', data)


def categoriaProyectos(request):
    categorias = CategoriaProyecto.objects.all()
    
    if request.method == 'POST':
        form = CategoriaProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = form.errors.as_json()
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    
    form = CategoriaProyectoForm()
    
    contexto = {'categorias': categorias, 'form': form}
    return render(request, 'proyectos/categoriaProyectos.html', contexto)

def eliminarCategoria(request, id_categoria):
    categoria = CategoriaProyecto.objects.get(id_categoria=id_categoria)
    categoria.delete()
    return redirect('categoriaproyecto')

def editarCategoria(request, id_categoria):
    categoria = CategoriaProyecto.objects.get(id_categoria=id_categoria)
    data = {
        'form': CategoriaProyectoForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaProyectoForm(data=request.POST, instance=categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('categoriaproyecto')
        else:
            data['form'] = formulario
    
    return render(request, 'proyectos/editarcategoria.html', data)


class ListarAvances(ListView):
    model = Avances
    template_name = 'avances/avances.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'listarAv':
                data = []
                for i in Avances.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Avances'
        context['create_url'] = reverse_lazy('agregarAvances')
        context['list_url'] = reverse_lazy('listarAvances')
        context['entity'] = 'Avances'
        return context
    

def agregarAvances(request):
    data = {
        'addavance': AvanceForm()  # No es necesario pasar request.FILES aquí
    }

    if request.method == 'POST':
        formulario = AvanceForm(request.POST, request.FILES)  # Aquí pasa ambos request.POST y request.FILES
        if formulario.is_valid():
            formulario.save()
            return redirect('avances')
        else:
            data['addavance'] = formulario

    return render(request, 'avances/agregarAvances.html', data)

def editarAvances(request, avance_id):
    avance = Avances.objects.get(avance_id=avance_id)
    data = {
        'form': AvanceForm(instance=avance)
    }
    if request.method == 'POST':
        formulario = AvanceForm(request.POST, request.FILES, instance=avance)
        if formulario.is_valid():
            formulario.save()
            return redirect('avances')
        else:
            data['form'] = formulario
    
    return render(request, 'avances/editarAvance.html', data)

def eliminarAvances(request, avance_id):
    avance = Avances.objects.get(avance_id=avance_id)
    avance.delete()
    return redirect('avances')

## MODULO COTIZACIONES

#LISTAR COTIZACIONES

class CotListView(ListView):
    model = Cotizaciones
    template_name = 'cotizaciones/listarCotizaciones.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'listarCot':
                data = []
                for i in Cotizaciones.objects.all():
                    data.append(i.toJSON())
            elif action == 'detalleCot':
                data = []
                for i in DetalleCotizaciones.objects.filter(id_cotizacion=request.POST['id_cotizacion']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cotizaciones'
        context['create_url'] = reverse_lazy('agregarCotizacion')
        context['list_url'] = reverse_lazy('listarCotizaciones')
        context['entity'] = 'Cotizaciones'
        return context

# CREAR COTIZACION

class CotView(CreateView):
    model = Cotizaciones
    form_class = CotizacionesForm
    template_name = 'cotizaciones/agregarCotizacion.html'
    success_url = reverse_lazy('listarCotizaciones')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Productos.objects.filter(nombre_producto__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.nombre_producto
                    data.append(item)
            elif action == 'add':

                # Cotizaciones
                vents = json.loads(request.POST['vents'])
                cotizacion = Cotizaciones()
                cotizacion.fecha_cotizacion = vents['fecha_cotizacion']
                cliente_id = int(vents['cli'])
                cotizacion.cliente = Clientes.objects.get(rut_cliente=cliente_id)
                metodo_pago = vents['metodo_pago']
                cotizacion.metodopago = MetodoPago.objects.get(id_metodopago=metodo_pago)
                cotizacion.subtotal = vents['subtotal']
                cotizacion.iva = vents['iva']
                cotizacion.total = vents['total']
                cotizacion.nombre_cotizacion = vents['nombre_cotizacion']
                cotizacion.comentario = vents['comentario']
                cotizacion.save()
                # Detalle
                for i in vents['products']:
                    det = DetalleCotizaciones()
                    det.id_cotizacion = cotizacion
                    product_id = i['id_producto']  # ID del producto
                    product_instance = Productos.objects.get(id_producto=product_id)  # Buscar la instancia de Productos
                    det.producto = product_instance  # Asignar la instancia
                    det.cantidad = int(i['cant'])
                    det.precio = float(i['precio_venta'])
                    det.subtotal = float(i['subtotal'])
                    det.save()
            elif action == 'create_client':
                data = []
                cliente = Clientes()
                cliente.rut_cliente = request.POST['rut_cliente']
                cliente.nombre = request.POST['nombre']
                cliente.apellido = request.POST['apellido']
                cliente.direccion = request.POST['direccion']
                cliente.telefono = request.POST['telefono']
                cliente.save()
                data.append(cliente.toJSON())
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Cotizacion'
        context['entity'] = 'Cotizaciones'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        context['frmClient'] = ClientesForm()
        return context

# EDITAR COTIZACION

class CotUpdateView(UpdateView):
    model = Cotizaciones
    form_class = CotizacionesForm
    template_name = 'cotizaciones/agregarCotizacion.html'
    success_url = reverse_lazy('listarCotizaciones')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                data = []
                prods = Productos.objects.filter(nombre_producto__icontains=request.POST['term'])[0:10]
                for i in prods:
                    item = i.toJSON()
                    item['value'] = i.nombre_producto
                    data.append(item)
            elif action == 'edit':
                
                # Cotizaciones
                vents = json.loads(request.POST['vents'])
                cotizacion = self.get_object()
                cotizacion.fecha_cotizacion = vents['fecha_cotizacion']
                cliente_id = int(vents['cli'])
                cotizacion.cliente = Clientes.objects.get(rut_cliente=cliente_id)
                metodo_pago = vents['metodo_pago']
                cotizacion.metodopago = MetodoPago.objects.get(id_metodopago=metodo_pago)
                cotizacion.subtotal = vents['subtotal']
                cotizacion.iva = vents['iva']
                cotizacion.total = vents['total']
                cotizacion.nombre_cotizacion = vents['nombre_cotizacion']
                cotizacion.comentario = vents['comentario']
                cotizacion.save()
                cotizacion.detallecotizaciones_set.all().delete()
                # Detalle
                for i in vents['products']:
                    det = DetalleCotizaciones()
                    det.id_cotizacion = cotizacion
                    product_id = i['id_producto']  # ID del producto
                    product_instance = Productos.objects.get(id_producto=product_id)  # Buscar la instancia de Productos
                    det.producto = product_instance  # Asignar la instancia
                    det.cantidad = int(i['cant'])
                    det.precio = float(i['precio_venta'])
                    det.subtotal = float(i['subtotal'])
                    det.save()
            elif action == 'create_client':
                data = []
                cliente = Clientes()
                cliente.rut_cliente = request.POST['rut_cliente']
                cliente.nombre = request.POST['nombre']
                cliente.apellido = request.POST['apellido']
                cliente.direccion = request.POST['direccion']
                cliente.telefono = request.POST['telefono']
                cliente.save()
                data.append(cliente.toJSON())
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_details_product(self):
        data = []
        try:
            for i in DetalleCotizaciones.objects.filter(id_cotizacion=self.get_object().id_cotizacion):
                item = i.producto.toJSON()
                item['cant'] = i.cantidad
                data.append(item)
        except:
            pass
        return data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de Cotizacion'
        context['entity'] = 'Cotizaciones'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['det'] = json.dumps(self.get_details_product())
        context['frmClient'] = ClientesForm()
        return context

# ELIMINAR COTIZACION 
def eliminarCotizaciones(request, id_cotizacion):
    cotizacion = Cotizaciones.objects.get(id_cotizacion=id_cotizacion)
    cotizacion.delete()
    return redirect('listarCotizaciones')

# GENERA PDF COTIZACION 

class CotizacionesPDF(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('cotizaciones/cotizacionpdf.html')
            context = {
                'cotizaciones': Cotizaciones.objects.get(id_cotizacion=kwargs['pk']),
                'comp': {'nombre': 'Gabinet Center', 'rut': '123456789', 'direccion': 'Virgen del Pilar 0389', 'ciudad': 'Santiago'},
            }
            html = template.render(context)
            
            nombre_archivo_cliente = 'Cotizacion' + ' ' + str(Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).cliente.nombre + ' ' 
            + Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).cliente.apellido + '-' + str(Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).nombre_cotizacion)
            + '-' + str(Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).fecha_cotizacion)) + '.pdf'
            
            # Ruta de destino en la carpeta de medios
            destino_pdf = os.path.join(settings.MEDIA_ROOT, 'pdfcot', nombre_archivo_cliente)

            pisaStatus = pisa.CreatePDF(html, open(destino_pdf, "wb"))
            
            # Asegúrate de que el PDF se haya creado con éxito antes de devolver la respuesta
            if pisaStatus.err:
                return HttpResponse("Error al generar el PDF", content_type='text/plain')
            
            # Construye la URL de descarga para el PDF en la carpeta de medios
            response = FileResponse(open(destino_pdf, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{nombre_archivo_cliente}"'

            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('listarCotizaciones'))
# MODULO CLIENTES
def listarClientes(request):
    clientes = Clientes.objects.all()

    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = form.errors.as_json()
            return JsonResponse({'errors': form.errors.as_json()}, status=400)
    
    form = ClientesForm()
    contexto = {
        'form': form,
        'clientes': clientes
    }
    return render(request, 'clientes/listarCliente.html', contexto)


def agregarClientes(request):
    data = {
        'addcli': ClientesForm()
    }
    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = formulario.errors.as_json()
            return JsonResponse({'errors': formulario.errors.as_json()}, status=400)

    return render(request, 'clientes/agregarCliente.html', data)


def eliminarClientes(request, rut_cliente):
    cliente = Clientes.objects.get(rut_cliente=rut_cliente)
    cliente.delete()
    return redirect('listarClientes')

def editarClientes(request, rut_cliente):
    cliente = Clientes.objects.get(rut_cliente=rut_cliente)
    data = {
        'addcli': ClientesForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarClientes')
        else:
            data['addcli'] = formulario

    return render(request, 'clientes/editarCliente.html', data)


# MODULO PRODUCTOS

class ProductosListView(ListView):
    model = Productos
    template_name = 'productos/listarProductos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'listarProductos':
                data = []
                for i in Productos.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('agregarProductos')
        context['list_url'] = reverse_lazy('listarProductos')
        context['entity'] = 'Productos'
        return context
            
def agregarProductos(request):
    data = {
        'addpro': ProductosForm()
    }
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('agregarProductos')
        else:
            data['addpro'] = formulario
    
    return render(request, 'productos/agregarProductos.html', data)

def eliminarProductos(request, id_producto):
    pro = Productos.objects.get(id_producto=id_producto)
    pro.delete()
    return redirect('listarProductos')


def editarProductos(request, id_producto):
    pro = Productos.objects.get(id_producto=id_producto)
    data = {
        'editpro': ProductosForm(instance=pro)
    }
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, instance=pro)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarProductos')
        else:
            data['editpro'] = formulario
    return render(request, 'productos/editarProductos.html', data)


            
def agregarCatySubcat (request):
    data = {
        'addcat': CatForm(),
        'addsubcat': SubCatForm()
    }
    if request.method == 'POST':
        formulario = CatForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarCatySubcat')
        else:
            data['addcat', 'addsubcat'] = formulario

    
    return render(request, 'productos/agregarCatySubcat.html', data)


def categoriaProd(request):
    catprod = CategoriaProductos.objects.all()

    if request.method == 'POST':
        formulario = CatForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = formulario.errors.as_json()
            return JsonResponse({'errors': formulario.errors.as_json()}, status=400)
    
    formulario = CatForm()
    contexto = {'catprod': catprod, 'formulario': formulario}
    return render(request, 'productos/categorias.html', contexto)

def eliCat(request, id_categoria):
    cat = CategoriaProductos.objects.get(id_categoria=id_categoria)
    cat.delete()
    return redirect('catproductos')

def editarCat(request, id_categoria):
    cat = CategoriaProductos.objects.get(id_categoria=id_categoria)
    data = {
        'editcat': CatForm(instance=cat)
    }
    if request.method == 'POST':
        formulario = CatForm(data=request.POST, instance=cat)
        if formulario.is_valid():
            formulario.save()
            return redirect('catproductos')
        else:
            data['editcat'] = formulario
    return render(request, 'productos/editarCat.html', data)


def subCat(request):
    subcat = SubcategoriaProductos.objects.all()

    if request.method == 'POST':
        formulario = SubCatForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = formulario.errors.as_json()
            return JsonResponse({'errors': formulario.errors.as_json()}, status=400)
    
    formulario = SubCatForm()
    contexto = {'subcat': subcat, 'formulario': formulario}
    return render(request, 'productos/subcategorias.html', contexto)

def eliSubCat(request, id_subcategoria):
    sub = SubcategoriaProductos.objects.get(id_subcategoria=id_subcategoria)
    sub.delete()
    return redirect('subcatproductos')

def editarSubCat(request, id_subcategoria):
    sub = SubcategoriaProductos.objects.get(id_subcategoria=id_subcategoria)
    data = {
        'editsubcat': SubCatForm(instance=sub)
    }
    if request.method == 'POST':
        formulario = SubCatForm(data=request.POST, instance=sub)
        if formulario.is_valid():
            formulario.save()
            return redirect('subcatproductos')
        else:
            data['editsubcat'] = formulario
    return render(request, 'productos/editarSubCat.html', data)


def marcaProd(request):
    marcaprod = MarcaProductos.objects.all()

    if request.method == 'POST':
        formulario = MarcaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = formulario.errors.as_json()
            return JsonResponse({'errors': formulario.errors.as_json()}, status=400)
    
    formulario = MarcaForm()
    contexto = {'marcaprod': marcaprod, 'formulario': formulario}
    return render(request, 'productos/marcas.html', contexto)

def eliMarca(request, id_marca):
    mar = MarcaProductos.objects.get(id_marca=id_marca)
    mar.delete()
    return redirect('marcaproductos')

def editarMarca(request, id_marca):
    mar = MarcaProductos.objects.get(id_marca=id_marca)
    data = {
        'editmar': MarcaForm(instance=mar)
    }
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=mar)
        if formulario.is_valid():
            formulario.save()
            return redirect('marcaproductos')
        else:
            data['editmar'] = formulario
    return render(request, 'productos/editarMarca.html', data)

def catSubMar(request):
    categorias = CategoriaProductos.objects.all()
    subcategorias = SubcategoriaProductos.objects.all()
    marcas = MarcaProductos.objects.all()
    
    contexto = {
        'cat': categorias,
        'subcat': subcategorias,
        'mar': marcas
    }
    return render(request, 'productos/todas.html', contexto)


def statusTarea(request):
    status = StatusTarea.objects.all()

    if request.method == 'POST':
        formulario = StatusTareaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'message': 'Registro exitoso.'})
        else:
            error_messages = formulario.errors.as_json()
            return JsonResponse({'errors': formulario.errors.as_json()}, status=400)
    
    formulario = StatusTareaForm()
    contexto = {'status': status, 'formulario': formulario}

    return render(request, 'equipos/statusTarea.html', contexto)

def eliStatus(request, id_status_tarea):
    status = StatusTarea.objects.get(id_status_tarea=id_status_tarea)
    status.delete()
    return redirect('statusTareas')

def editarStatus(request, id_status_tarea):
    status = StatusTarea.objects.get(id_status_tarea=id_status_tarea)
    data = {
        'editstatustarea': StatusTareaForm(instance=status)
    }
    if request.method == 'POST':
        formulario = StatusTareaForm(data=request.POST, instance=status)
        if formulario.is_valid():
            formulario.save()
            return redirect('statusTareas')
        else:
            data['editstatustarea'] = formulario
    return render(request, 'equipos/editarStatus.html', data)


# MODULO EQUIPOS

class Equipo(CreateView):
    model = Equipos
    form_class = EquiposForm
    template_name = 'equipos/agregarEquipos.html'
    success_url = reverse_lazy('listarEquipos')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_trabajador':
                data = []
                trab = User.objects.filter(first_name__icontains=request.POST['term'])[0:10]
                for i in trab:
                    item = i.toJSON()
                    item['value'] = i.first_name + ' ' + i.last_name
                    data.append(item)
            elif action == 'add':
                equipoj = json.loads(request.POST['equipo'])
                equipo = Equipos()
                equipo.proyecto_id_proyecto = Proyecto.objects.get(id_proyecto=equipoj['proyecto_id_proyecto'])
                equipo.nombre_equipo = equipoj['nombre_equipo']
                equipo.observaciones = equipoj['observaciones']
                equipo.save()
                for i in equipoj['trabajadores']:
                    det = DetalleEquipo()
                    det.id_equipo = equipo
                    trabajador_id = i['rut']
                    trabajador_instance = User.objects.get(rut=trabajador_id)
                    det.trabajador = trabajador_instance
                    det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Equipo'
        context['entity'] = 'Equipos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context

class EquipoEdit(UpdateView):
    model = Equipos
    form_class = EquiposForm
    template_name = 'equipos/agregarEquipos.html'
    success_url = reverse_lazy('listarEquipos')
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'buscar_trabajador':
                data = []
                trab = User.objects.filter(first_name__icontains=request.POST['term'])[0:10]
                for i in trab:
                    item = i.toJSON()
                    item['value'] = i.first_name + ' ' + i.last_name
                    data.append(item)
            elif action == 'edit':
                equipoj = json.loads(request.POST['equipo'])
                equipo = self.get_object()
                equipo.proyecto_id_proyecto = Proyecto.objects.get(id_proyecto=equipoj['proyecto_id_proyecto'])
                equipo.nombre_equipo = equipoj['nombre_equipo']
                equipo.observaciones = equipoj['observaciones']
                equipo.save()
                equipo.detalleequipo_set.all().delete()
                for i in equipoj['trabajadores']:
                    det = DetalleEquipo()
                    det.id_equipo = equipo
                    trabajador_id = i['rut']
                    trabajador_instance = User.objects.get(rut=trabajador_id)
                    det.trabajador = trabajador_instance
                    det.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_detalles_equipo(self):
        data = []
        try:
            for i in DetalleEquipo.objects.filter(id_equipo=self.get_object().id_equipo):
                item = i.trabajador.toJSON()
                data.append(item)
        except:
            pass
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de Equipo'
        context['entity'] = 'Equipos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        context['det'] = json.dumps(self.get_detalles_equipo())
        return context

class EquipoListView(ListView):
    model = Equipos
    template_name = 'equipos/listarEquipos.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'listarEq':
                data = []
                for i in Equipos.objects.all():
                    data.append(i.toJSON())
            elif action == 'detalleEquipo':
                data = []
                for i in DetalleEquipo.objects.filter(id_equipo=request.POST['id_equipo']):
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Equipos'
        context['create_url'] = reverse_lazy('agregarEquipos')
        context['list_url'] = reverse_lazy('listarEquipos')
        context['entity'] = 'Equipos'
        return context


def EliminarEquipo(request, id_equipo):
    equipo = Equipos.objects.get(id_equipo=id_equipo)
    equipo.delete()
    return redirect('listarEquipos')

# Modulo Tareas

class TareasListView(ListView):
    model = Tareas
    template_name = 'equipos/listarTareas.html'
    form = TareasForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'listarTareas':
                data = []
                for i in Tareas.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Tareas'
        context['create_url'] = reverse_lazy('agregarTareas')
        context['list_url'] = reverse_lazy('listarTareas')
        context['entity'] = 'Tareas'
        return context



def agregarTareas(request):
    if request.method == 'POST':
        form = TareasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarTareas')
    else:
        form = TareasForm()
    return render(request, 'equipos/agregarTareas.html', {'form': form})


def editarTareas(request, tarea_id):
    tarea = Tareas.objects.get(tarea_id=tarea_id)
    data = {
        'form': TareasForm(instance=tarea)
    }
    if request.method == 'POST':
        formulario = TareasForm(data=request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarTareas')
        else:
            data['form'] = formulario
    return render(request, 'equipos/editarTareas.html', data)


def eliminarTareas(request, tarea_id):
    
    tarea = Tareas.objects.get(tarea_id=tarea_id)
    tarea.delete()
    return redirect('listarTareas')


