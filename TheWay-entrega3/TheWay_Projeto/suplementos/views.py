from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ConsultaSuplemento
from .forms import SuplementoForm

def recomendacao_view(request):
    resultado = None
    form = SuplementoForm()

    if request.method == 'POST':
        form = SuplementoForm(request.POST)
        if form.is_valid():
            consulta = form.save()
            resultado = consulta
        else:
            messages.error(request, "Por favor, corrija os erros abaixo.")

    return render(request, 'suplementos/recomendacao.html', {
        'form': form,
        'resultado': resultado,
    })

def frontend_view(request):
    return render(request, 'suplementos/frontend.html')
