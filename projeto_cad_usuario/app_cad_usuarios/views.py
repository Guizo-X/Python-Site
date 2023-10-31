from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    # exibir todos os usuarios cadastrados numa nova pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    # Retornar os dados para a pagina de listagem de usuários
    return render(request,'usuarios/usuarios.html',usuarios)