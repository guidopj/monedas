from django.contrib import  messages

from .models import Moneda, Usuario, MonedasUsuario
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LoginForm, MonedaForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'monedas/login.html', context)

def home(request,user):
    return render(request, 'monedas/home.html', {'user' : user})

def crearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            contrasena = form.cleaned_data['contrasena']
            user.set_password = contrasena
            user.save()
            messages.error(request, "Usuario " + user.nombreUsuario + " creado correctamente")
            return redirect('index')
        else:
            context = {'errors': form.errors}
            return render(request, 'monedas/crearUsuario.html', context)

    else:
        form = UsuarioForm()
        context = {'form': form}
        return render(request, 'monedas/crearUsuario.html', context)

def autenticarUsuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombreUsuario = form.cleaned_data['nombreUsuario']
            contrasena = form.cleaned_data['contrasena']
            try:
                user = Usuario.objects.get(nombreUsuario=nombreUsuario)
                login(request, user)
                context = {'user': nombreUsuario, 'monedas': obtenerMonedas()}
                #return render(request, 'monedas/home.html', context)
                return redirect('home', context)
            except:
                messages.error(request, "Usuario " + nombreUsuario + " no existe")
                return redirect('index')
        else:
            return render(request, 'monedas/login.html', {'errors' : form.errors})




def obtenerMonedas():
    return Moneda.objects.all()