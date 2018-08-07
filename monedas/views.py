from django.core.exceptions import ValidationError

from .models import Moneda, Usuario, MonedasUsuario
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LoginForm, MonedaForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'monedas/login.html', context)

def autenticarUsuario(request):
    nombre = request.POST['nombreUsuario']
    contrasena = request.POST['contrasena']
    user = Usuario.objects.get(nombreUsuario=nombre)
    if not user:
        raise ValidationError("Usuario no existe")
    else:
        context = {'user' : user}
        return render(request, 'monedas/home.html')

def obtenerMonedas(request):
    monedas = Moneda.objects.all()
    contexto = {'monedas': monedas}

    return render(request, 'monedas/login.html', contexto)


def crearMoneda(request, nombreUsuario):
    if request.method == 'POST':
        form = MonedaForm(request.POST)
        if form.is_valid():
            nuevaMoneda = Moneda(nombreMoneda=form.cleaned_data['nombreMoneda'],
                                 signo=form.cleaned_data['signo'],
                                 userName=nombreUsuario)
            nuevaMoneda.save()
            return redirect('home')
    else:
        form = MonedaForm()
        context = {'nombreUsuario': nombreUsuario}
        return render(request, 'monedas/crearMoneda.html', context)



def crearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            userName = form.cleaned_data['nombreUsuario']
            contrasena = form.cleaned_data['contrasena']
            user = authenticate(username=userName, password=contrasena)
            login(request, user)
            return redirect('home', {'user': user})
        else:
            context = {'errors': form.errors}
            return render(request, 'monedas/crearUsuario.html', context)

    else:
        form = UsuarioForm()
        context = {'form': form}
        return render(request, 'monedas/crearUsuario.html', context)

def enviarMonedas(request, usuarioEnvia):
    if request.method == 'POST':
        #usuarioEnvia = MonedasUsuario.objects.get(userName=userName1,moneda=mon)
        usuarioRecibe = request.POST.get("usuarioRecibe", "")
        moneda = request.POST.get("moneda", "")
        cantidad = request.POST.get("cant", "")
        usuarioEnvia.enviarMonedas(usuarioRecibe,moneda,cantidad)
        usuarioEnvia.save()
        usuarioRecibe.save()
        nuevoHistorial = {'usuarioEnvia': usuarioEnvia, 'usuarioRecibe' :usuarioRecibe, 'moneda' : mon, 'cantidad' : cant}
        return render(request, 'monedas/home.html', nuevoHistorial)
    else:
        context = {'user' :usuarioEnvia}
        return render(request, 'monedas/enviarMoneda.html', context)