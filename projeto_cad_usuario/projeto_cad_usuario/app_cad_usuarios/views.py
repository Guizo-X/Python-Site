from django import forms

class UsuarioForm(forms.Form):
    nome = forms.CharField(max_length=255)
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)

# Em sua view, importe o formulário e utilize-o para validar os dados de entrada:
from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['senha']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirecionar para a página após o login bem-sucedido
            return redirect('home')
        else:
             return HttpResponse('email ou senha invalidos')
   
    return render(request, 'usuarios/login.html')

def usuarios(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            if Usuario.objects.filter(nome=nome).exists() or Usuario.objects.filter(email=email).exists():
                return HttpResponse('Já existe um usuário com esse nome ou e-mail')

            novo_usuario = Usuario(nome=nome, email=email, senha=senha)
            novo_usuario.save()
            return HttpResponse('Usuário cadastrado com sucesso')

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)
    


