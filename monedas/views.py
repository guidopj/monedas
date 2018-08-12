from django.contrib import messages

from .models import Moneda, Usuario, MonedasUsuario
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LoginForm, MonedaForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'monedas/login.html', context)


def home(request, user):
    return render(request, 'monedas/home.html', {'user': user})


def crearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Usuario " + user.nombreUsuario + " creado correctamente")
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
                return redirect(home, user=nombreUsuario)
            except:
                messages.error(request, "Usuario " + nombreUsuario + " no existe")
                return redirect('index')
        else:
            return render(request, 'monedas/login.html', {'errors': form.errors})


def obtenerMonedas():
    return Moneda.objects.all()


def crearMoneda(request, user):
    if request.method == 'POST':
        form = MonedaForm(request.POST)
        if form.is_valid():
            moneda = form.save(commit=False)
            user = Usuario.objects.get(nombreUsuario=user)
            moneda.creadaPor = user
            moneda.save()
            messages.success(request, "Moneda" + moneda.nombreMoneda + " creada correctamente")
        else:
            messages.error(request, "Error en la creacion de moneda")
        return HttpResponseRedirect("")
    else:
        # user = Usuario.objects.get(nombreUsuario=username)
        form = MonedaForm()
        context = {'form': form, 'user': user}
        return render(request, 'monedas/crearMoneda.html', context)
