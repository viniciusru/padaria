# from django.shortcuts import render
from urllib import request
from django.shortcuts import render;
from .models import Usuarios

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(requets):
    # Salvar dados no banco de dados
    novo_usuario = usuarios()
    novo_usuario.nomo = requets.POST.get('nome')
    novo_usuario.pedidos = requets.POST.get('pedidos')
    novo_usuario.save()
    
    usuarios = {
        'usuarios':usuarios.objects.all()
        }
    return render(requets, 'usuarios/pedidos.html', usuarios)
    