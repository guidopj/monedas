from django.shortcuts import render
from .forms import MonedaForm
from .models import Moneda
from django.shortcuts import redirect
from .forms import UsuarioForm
from .models import Usuario
from .forms import LoginForm

def index(request):
    if request.method == 'POST':
        form = MonedaForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = LoginForm()

    contexto = {'form': form}

    return render(request, 'monedas/index.html', contexto)

def obtenerMonedas(request):
    monedas = Moneda.objects.all()
    contexto = {'monedas': monedas}

    return render(request, 'monedas/index.html', contexto)


def crearMoneda(request):
    if request.method == 'POST':
        form = MonedaForm(request.POST)
        if form.is_valid():
            nuevaMoneda = Moneda(nombreMoneda=form.cleaned_data['nombreMoneda'],
                                 signo=form.cleaned_data['signo'])
            nuevaMoneda.save()
            return redirect('index')
    else:
        form = MonedaForm()
        context = {'form': form}
        return render(request, 'monedas/crearMoneda.html', context)


def crearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            nuevoUsuario = Usuario(nombreUsuario=form.cleaned_data['nombreUsuario'],
                                  contrasena=form.cleaned_data['contrasena'],
                                  nombre=form.cleaned_data['nombre'],
                                  apellido=form.cleaned_data['apellido'],
                                  fecha_nac=form.cleaned_data['fecha_nac'])
            nuevoUsuario.save()
            return render('monedas/home.html', context)
        else:
            return render(request, 'monedas/crearUsuario.html', context)
    else:
        form = UsuarioForm()
        context = {'form': form}
        return render(request, 'monedas/crearUsuario.html', context)