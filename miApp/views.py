from django.shortcuts import render, redirect, get_object_or_404
from miApp.models import Rifas, Premios, Participante, Venta
from miApp.forms import FormVenta
from django.db.models import F
from django.http import Http404
import random
from django.http import JsonResponse
from django.db.models import Count


def Index(req):
    rifa = Rifas.objects.all()
    data = {'rifa': rifa}
    return render(req, "Index.html", data)


def comprar(req, id):
    form = FormVenta()
    form.fields['id_rifa'].initial = id

    if req.method == 'POST':
        form = FormVenta(req.POST)
        if form.is_valid():
            rifas = Rifas.objects.get(id=id)

            cantidad = form.cleaned_data['numero_compra']
            rifas.numeros_disponibles -= cantidad
            rifas.numeros_vendidos += cantidad
            rifas.save()

            venta = Venta()
            venta.rifas = rifas
            venta.nombre = form.cleaned_data['nombre']
            venta.email = form.cleaned_data['email']
            venta.telefono = form.cleaned_data['telefono']
            venta.numero_compra = form.cleaned_data['numero_compra']
            venta.codigo = form.cleaned_data['codigo']

            venta.save()
            return redirect('/ticket/' + str(rifas.id))

    try:
        rifas = Rifas.objects.get(id=id)
        data = {'rifas': rifas,
                'form': form
                }
        return render(req, 'comprar.html', data)
    except:
        raise UserWarning("Error, Rifa no existe")


def detalle_premio(req, rifas_id):
    try:
        rifas = get_object_or_404(Rifas, id=rifas_id)
        premios = Premios.objects.filter(rifas=rifas)
        data = {'premio': premios, 'rifas': rifas}
        return render(req, 'Premios.html', data)

    except Rifas.DoesNotExist:
        raise Http404("No existe la rifa con el ID proporcionado")
    except Premios.DoesNotExist:
        raise Http404("No hay premios asociados a la rifa")


def sorteo(request):
    participantes = Participante.objects.all()

    ganadores = participantes.filter(winner=True)

    data = {'participantes': participantes, 'ganadores': ganadores}

    return render(request, 'Sorteo.html', data)