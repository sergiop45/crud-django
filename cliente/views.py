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

def editar(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'update.html', {'cliente': cliente})

def update(request, id):
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    cliente = Cliente .objects.get(id=id)
    cliente.nome = nome
    cliente.sobrenome = sobrenome
    cliente.save()
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})

def deletar(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})