from django.shortcuts import render, redirect
from Sicos40.forms import ClienteForm
from Sicos40.forms import BusquedaForm
from Sicos40.models import Cliente
from .models import Poliza
from django.http import JsonResponse
from django.db.models import Q



# Create your views here.
def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()

    # Agrega un mensaje de éxito a la variable de contexto
    success_message = "¡Registro guardado con éxito!"
    return render(request, 'paginas/clientes.html', {'form': form, 'success_message': success_message})

def panel(request):
    resultados = None
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            tipo_busqueda = form.cleaned_data['tipo_busqueda']
            criterio_busqueda = form.cleaned_data['criterio_busqueda']

            if tipo_busqueda == 'cliente':
                clientes = Cliente.objects.filter(Q(Apellidos__icontains=criterio_busqueda) | Q(Nombres__icontains=criterio_busqueda))
                resultados = [
                    {
                        'cliente': cliente,
                        'polizas': Poliza.objects.filter(IdCliente=cliente.IdCliente)
                    }
                    for cliente in clientes
                ]
            else:
                polizas = Poliza.objects.filter(NumeroPoliza__icontains=criterio_busqueda)
                resultados = [
                    {
                        'poliza': poliza,
                        'cliente': poliza.IdCliente  # Asegúrate de usar la relación ForeignKey correctamente
                    }
                    for poliza in polizas
                ]
    else:
        form = BusquedaForm()

    return render(request, 'paginas/panel.html', {'form': form, 'resultados': resultados})

def obtener_polizas(request, id_cliente):
    polizas = Poliza.objects.filter(IdCliente=id_cliente)
    data = {'polizas': list(polizas.values('IdPoliza', 'NumeroPoliza'))}
    return JsonResponse(data)