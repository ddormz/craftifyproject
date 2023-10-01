from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from .models import User

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