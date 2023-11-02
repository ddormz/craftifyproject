import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, UpdateView, View
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from datetime import datetime
# Create your views here.

@login_required
def home(request ):
    return render(request, 'core/home.html')

@login_required
def products(request):
    return render(request, 'core/products.html')

def exit(request):
    logout(request)
    return redirect('login')



@login_required
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
@login_required
def verproyectos(request):
    proyectos = Proyecto.objects.all()
    fecha_actual = datetime.now()  # Obtenemos la fecha actual

    for proyecto in proyectos:
        fecha_creacion = proyecto.fecha
        plazo_entrega = proyecto.plazo_entrega

        if fecha_creacion and plazo_entrega:
            fecha_creacion = datetime.combine(fecha_creacion, datetime.min.time())
            plazo_entrega = datetime.combine(plazo_entrega, datetime.min.time())

            tiempo_restante = (plazo_entrega - fecha_actual).days
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
            return redirect('proyectos')
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

def statusProyectos(request):
    proyecto = Proyecto.objects.all()
    contexto = {'proyectos':proyecto}
    return render(request, 'proyectos/statusProyectos.html', contexto)


def avances(request):
    avance = Avances.objects.all()
    contexto = {'avances':avance}
    return render(request, 'avances/avances.html', contexto)

def agregarAvances(request):
    data = {
        'addavance': AvanceForm(request.FILES)
    }
    if request.method == 'POST':
        formulario = AvanceForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('avances')
        else:
            data['addavance'] = formulario
    return render (request, 'avances/agregarAvances.html', data)
        

## Vista por Clases Cotizaciones (Listar)

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

## Vista por Clases Cotizaciones (Crear)

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
        return context


# VISTA POR CLASE EDITAR 

class CotUpdateView(UpdateView):
    model = Cotizaciones
    form_class = CotizacionesForm
    template_name = 'cotizaciones/agregarCotizacion.html'
    #success_url = reverse_lazy('listarCotizaciones')
    #url_redirect = success_url

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
        return context



# ELIMINAR COTIZACION 

def eliminarCotizaciones(request, id_cotizacion):
    cotizacion = Cotizaciones.objects.get(id_cotizacion=id_cotizacion)
    cotizacion.delete()
    return redirect('listarCotizaciones')
def listarClientes(request):
    cliente = Clientes.objects.all()
    contexto = {'clientes':cliente}
    return render(request, 'clientes/listarCliente.html', contexto)
def agregarClientes(request):
    data = {
        'addcli': ClientesForm()
    }
    if request.method == 'POST':
        formulario = ClientesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarClientes')
        else:
            data['addcli'] = formulario

    return render(request, 'clientes/agregarCliente.html', data)


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
            # Create a Django response object, and specify content_type as pdf
            response = HttpResponse(content_type='application/pdf')
            nombre_archivo_cliente = 'Cotizacion' + ' ' + str(Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).cliente.nombre + ' ' 
            + Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).cliente.apellido + '-' + str(Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).nombre_cotizacion)
            + '-' + str(Cotizaciones.objects.get(id_cotizacion=kwargs['pk']).fecha_cotizacion)) + '.pdf'
            response['Content-Disposition'] = 'attachment; filename=%s' % nombre_archivo_cliente
            pisaStatus = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('listarCotizaciones'))



def listarProductos(request):
    productos = Productos.objects.all()
    contexto = {'productos':productos}
    return render(request, 'productos/listarProductos.html', contexto)
def agregarProductos(request):
    data = {
        'addpro': ProductosForm()
    }
    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarProductos')
        else:
            data['addpro'] = formulario
    
    return render(request, 'productos/agregarProductos.html', data)
def listarCatySubcat(request):
    categorias = CategoriaProductos.objects.all()
    subcategorias = SubcategoriaProductos.objects.all()
    contexto = {'categorias':categorias, 'subcategorias':subcategorias}
    return render(request, 'productos/listadoCategoriasProd.html', contexto)
            

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


# Modulo Equipos

def listarEquipos(request):
    equipos = Equipos.objects.all()
    contexto = {'equipos':equipos}
    return render(request, 'equipos/listarEquipos.html', contexto)


def agregarEquipos(request):
    data = {
        'addequi': EquiposForm()
    }
    if request.method == 'POST':
        formulario = EquiposForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarEquipos')
        else:
            data['addequi'] = formulario
    
    return render(request, 'equipos/agregarEquipos.html', data)


# Modulo Asignaciones 

def listarAsignaciones(request):
    asignaciones = EquipoAsignacion.objects.all()
    contexto = {'asignaciones':asignaciones}
    return render(request, 'equipos/listarAsignaciones.html', contexto)

def agregarAsignaciones(request):
    data = {
        'addasig': AsignacionForm()
    }
    if request.method == 'POST':
        formulario = AsignacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarAsignaciones')
        else:
            data['addasig'] = formulario
    
    return render(request, 'equipos/agregarAsignaciones.html', data)