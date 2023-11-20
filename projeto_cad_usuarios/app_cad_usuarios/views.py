# from django.shortcuts import render
from urllib import request
from django.shortcuts import render;
from .models import Usuarios

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(requets):
    # Salvar dados no banco de dados
    novo_usuario = Usuarios()
    novo_usuario.Nome = requets.POST.get('nome')
    novo_usuario.idade = requets.POST.get('pedidos')
    novo_usuario.save()
    
    usuarios = {
        'usuarios':Usuarios.objects.all()
        }
    return render(requets, 'usuarios/pedidos.html', Usuarios)
    