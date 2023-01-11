from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def crear_persona(request):

    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            print('Valid form')
            persona = form.save(commit=False)
            persona.user = request.user
            Persona.objects.filter(user = request.user).delete()
            persona.save()
            return redirect('../../')

    else:
        form = PersonaForm()
    return render(request, './formulario/formulario.html', {'form': form})