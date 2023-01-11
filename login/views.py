from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistroForm
from django.shortcuts import redirect

from django.contrib.auth import login

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            print('Valid form')
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            login(request, user)
            return redirect('../../')

    else:
        form = RegistroForm()
    return render(request, './login/registro_form.html', {'form': form})

