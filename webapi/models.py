from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(null=False, max_length=100)
    email = models.CharField(null=False, max_length=50)
    morada = models.CharField(null=False, max_length=130)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


