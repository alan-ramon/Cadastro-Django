from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome_completo

    
class Contato(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=256)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome