from django.shortcuts import render, redirect
from .models import Numero
import random

def gerar_numero(request):
    if request.method == "POST":
        novo_numero = random.randint(1, 1000)
        Numero.objects.create(valor=novo_numero)
        return redirect('index')

    numeros = Numero.objects.all().order_by('-criado_em')
    contador = numeros.count()
    return render(request, 'numeros/index.html', {'numeros': numeros, 'contador': contador})
