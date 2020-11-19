from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona, Club_Lectores
from .forms import FormularioPersona


def lista_registros(request) : 
    num_visitas = request.session.get('num_visitas', 1)
    num_visitas = num_visitas + 1
    request.session['num_visitas'] = num_visitas
    lista = Persona.objects.all() 
    return render(request, 'appUsuarios/registro_clientes.html', 
          {'lista' : lista, 'num_visitas' : num_visitas})

def lista_tarjetas(request) :
    tarjetas = Club_Lectores.objects.all()
    return render(request, 'appUsuarios/lista_tarjetas.html', 
           {'listaTarjetas' : tarjetas})

def tarjetas_saldo(request) :
    tarjetas = Club_Lectores.objects.filter(saldoDisponible__gte=1)
    return render(request, 'appUsuarios/lista_tarjetas.html', 
           {'listaTarjetas' : tarjetas})

def persona_nueva(request) :
    if request.method == 'POST':
        formulario = FormularioPersona(request.POST)
        if formulario.is_valid():
            persona = formulario.save(commit=False)
            persona.save()
            return HttpResponse('Registro realizado con exito')
    else:
        formulario = FormularioPersona()
    return render(request, 'appUsuarios/persona_nueva.html', {'form': formulario})