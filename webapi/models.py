from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(null=False, max_length=100)
    email = models.CharField(null=False, max_length=50)
    morada = models.CharField(null=False, max_length=130)
    unidade_medida = models.CharField(null=False, max_length=1000)
    localizacao_favorita = models.CharField(null=False, max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class Usuario_Historico_localizacoes(models.Model):
    idUsuario=models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    localizacao=models.CharField(null=False, max_length=130)
    data_de_pesquisa=models.DateField(auto_now_add=True)
