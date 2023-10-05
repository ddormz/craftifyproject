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

def register(request):

    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return redirect('register')
        else:
            data['form'] = user_creation_form
    return render(request, 'registration/register.html', data)

def listarTrabajadores(request):
    user = User.objects.all()
    contexto = {'users':user}
    return render(request, 'core/listarTrabajadores.html', contexto)


def editarTrabajadores(request, rut):
    user = User.objects.get(rut=rut)
    data = {
        'form': CustomUserCreationForm(instance=user)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=user)
        if formulario.is_valid():
            formulario.save()
            return redirect('listarTrabajadores')
        else:
            data['form'] = formulario

    return render(request, 'core/editarTrabajador.html', data)

def eliminarTrabajadores(request, rut):
    user = User.objects.get(rut=rut)
    user.delete()
    return redirect('listarTrabajadores')

def proyectos(request):
    proyecto = Proyecto.objects.all()
    contexto = {'proyectos':proyecto}
    return render(request, 'core/proyectos.html', contexto)

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
    
    return render(request, 'core/agregarProyecto.html', data)

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
    
    return render(request, 'core/editarProyecto.html', data)

def eliminarProyecto(request, id_proyecto):
    proyecto = Proyecto.objects.get(id_proyecto=id_proyecto)
    proyecto.delete()
    return redirect('proyectos')

def avances(request):
    avance = Avances.objects.all()
    contexto = {'avances':avance}
    return render(request, 'core/avances.html', contexto)
