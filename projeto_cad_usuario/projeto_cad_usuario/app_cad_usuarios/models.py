from django.db import models
from django.contrib.auth.hashers import make_password

def default_password():
    return make_password('senha_padrao')

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(default="example@example.com")
    senha = models.CharField(max_length=128, default=default_password)