from django.contrib import messages

from .models import Moneda, Usuario, MonedasUsuario, Historial
from django.core.exceptions import  ValidationError
from django.shortcuts import render, redirect
from .forms import UsuarioForm, LoginForm, MonedaForm, EnviarMonedasForm, ComprarMonedasForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def index(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'monedas/login.html', context)


def home(request, user):
    monedas = obtenerMonedas()
    return render(request, 'monedas/home.html', {'user': user, 'monedas' : monedas})


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
                user = Usuario.objects.get(nombreUsuario=nombreUsuario, contrasena=contrasena)
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
            Historial.objects.create(accion="creacion de Moneda",
                                     usuarioCreador=user,
                                     usuarioEnvia="",
                                     usuarioRecibe="",
                                     moneda=form.cleaned_data['nombreMoneda'],
                                     cantMonedas=0)
        else:
            messages.error(request, "Error en la creacion de moneda")
        return HttpResponseRedirect("")
    else:
        form = MonedaForm()
        context = {'form': form, 'user': user, 'titulo': 'Crear Nueva Moneda', 'urlParam': 'crearMoneda'}
        return render(request, 'monedas/monedas_template.html', context)


def comprarMonedas(request, user):
    if request.method == 'POST':
        form = ComprarMonedasForm(request.POST)
        if form.is_valid():
            nombreMoneda = form.cleaned_data['moneda']
            cantidad = form.cleaned_data['cantidad']
            usuario = Usuario.objects.get(nombreUsuario=user)
            try:
                usuario = MonedasUsuario.objects.get(moneda=nombreMoneda, usuario=usuario)
                usuario.cantMonedas = usuario.cantMonedas + cantidad
                usuario.save()
                messages.success(request, "Se suman monedas a lo que ya tenias")
            except MonedasUsuario.DoesNotExist:
                MonedasUsuario.objects.create(moneda=nombreMoneda, usuario=usuario, cantMonedas=cantidad)
                messages.success(request, "Comienza a tener este tipo de monedas")
            finally:
                Historial.objects.create(accion="compra de Moneda",
                                         usuarioCreador=user,
                                         usuarioEnvia="",
                                         usuarioRecibe="",
                                         moneda=form.cleaned_data['moneda'],
                                         cantMonedas=form.cleaned_data['cantidad'])
                return HttpResponseRedirect("")
        else:
            messages.error(request, "Error en la transaccion")
            return HttpResponse("NO!")
    else:
        form = ComprarMonedasForm()
        context = {'form': form, 'user': user, 'titulo': 'Comprar Monedas', 'urlParam': 'comprarMonedas'}
        return render(request, 'monedas/monedas_template.html', context)

def commitCambios(userEnvia,userRecibe,moneda,cantidad):
    userRecibe.save()
    userEnvia.save()
    Historial.objects.create(accion="Enviar Monedas",
                             usuarioCreador="",
                             usuarioEnvia=userEnvia.usuario,
                             usuarioRecibe=userRecibe.usuario,
                             moneda=moneda,
                             cantMonedas=cantidad)


def enviarMonedas(request, user):
    if request.method == 'POST':
        form = EnviarMonedasForm(request.POST)
        if form.is_valid():
            moneda, usuarioRecibe, cantidad = form.cleaned_data['moneda'], form.cleaned_data['usuario'], form.cleaned_data['cantidad']
            userEnvia = MonedasUsuario.objects.get(usuario=user, moneda=moneda)

            userRecibe = MonedasUsuario.objects.filter(moneda=moneda, usuario=usuarioRecibe)
            if userRecibe.count() > 0:
                try:
                    userRecibe = userRecibe.get()
                    userEnvia.enviarMonedasExistente(cantidad, userRecibe)
                    commitCambios(userEnvia, userRecibe, moneda, cantidad)
                except ValidationError:
                    messages.error(request, "No posee suficientes monedas")
            else:
                try:
                    userRecibe = userEnvia.enviarMonedasANuevo(cantidad, usuarioRecibe, moneda)
                    commitCambios(userEnvia, userRecibe, moneda, cantidad)
                except ValidationError:
                    messages.error(request, "No posee suficientes monedas")
            return HttpResponseRedirect("")
        else:
            return HttpResponse("Error en la creacion de moneda")
    else:
        form = EnviarMonedasForm()
        context = {'form': form, 'user': user, 'titulo': 'Enviar Monedas', 'urlParam': 'enviarMonedas'}
        return render(request, 'monedas/monedas_template.html', context)


def balance(request, user):
    monedasDeUsuario = MonedasUsuario.objects.filter(usuario=user)
    context = {'monedasDeUsuario': monedasDeUsuario, 'user': user}
    return render(request, 'monedas/balance.html', context)

def historial(request, user):
    historial = Historial.objects.all()
    context = {'historial': historial, 'user': user}
    return render(request, 'monedas/historial.html', context)
