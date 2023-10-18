from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import *
from .models import *

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




def listarTrabajadores(request):
    users = User.objects.all()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # Respuesta exitosa en formato JSON
        else:
            return JsonResponse({'success': False})  # Respuesta de error en formato JSON
    
    form = CustomUserCreationForm()
    
    contexto = {'users': users, 'form': form}
    return render(request, 'trabajadores/listarTrabajadores.html', contexto)




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

def eliminarTrabajadores(request, rut):
    user = User.objects.get(rut=rut)
    user.delete()
    return redirect('listarTrabajadores')

def proyectos(request):
    proyecto = Proyecto.objects.all()
    contexto = {'proyectos':proyecto}
    return render(request, 'proyectos/proyectos.html', contexto)

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
            return redirect('proyectos')
        else:
            data['form'] = formulario
    
    return render(request, 'proyectos/editarProyecto.html', data)

def eliminarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id_proyecto=id_proyecto)
    proyecto.delete()
    return redirect('proyectos')

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
        

def listarCotizaciones(request):
    cotizaciones = Cotizaciones.objects.all()
    contexto = {'cotizaciones':cotizaciones}
    return render(request, 'cotizaciones/listarCotizaciones.html', contexto)

def agregarCotizaciones(request):
    data = {
        'addcot': CotizacionesForm()
    }
    if request.method == 'POST':
        formulario = CotizacionesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarCotizaciones')
        else:
            data['addcot'] = formulario
    
    return render(request, 'cotizaciones/agregarCotizacion.html', data)

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