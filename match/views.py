from django.shortcuts import render
from formulario.models import Persona
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from Parejas.herramientas import calcularMatch

@login_required
def cargar_match(request):
    registro = False
    usuario = Persona.objects.filter(user = request.user)
    if len(usuario) == 1:
        registro = True
    else:
        return HttpResponse("Debes haber llenado el formulario con la encuesta para saber de ti y recomendarte amigos")
    # usuarios = Persona.objects.all()
    usuarios = Persona.objects.exclude(user = request.user)

    resultado = calcularMatch(usuario, usuarios)
    

    variables_de_template = {
        "registro": registro, 
        "usuarios": resultado
        }
    return render(request, './match/index.html', variables_de_template)