from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from formulario.models import Persona

# Create your views here.


@login_required
def index(request):
    registro = False
    if len(Persona.objects.filter(user = request.user)) == 1:
        registro = True

    return render(request, "main./index.html", {"registro": registro})