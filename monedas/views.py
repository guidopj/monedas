from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import MonedaForm
from .models import Moneda
from django.shortcuts import redirect
from django.http import HttpResponse

def index(request):
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
        return render(request, 'monedas/crearMoneda.html', context)  # context para usarlo en el html
        #return HttpResponse("fds")