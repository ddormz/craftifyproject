from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

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