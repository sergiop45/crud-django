from django.shortcuts import render
from .models import Cliente

# Create your views here.

def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {"clientes": clientes})

def salvar(request):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    Cliente.objects.create(nome=nome, sobrenome=sobrenome)
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})