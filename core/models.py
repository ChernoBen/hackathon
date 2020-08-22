
import uuid

from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    tipo = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.tipo

class Estados(models.Model):
    sigla = models.CharField(max_length=15)

    def __str__(self):
        return self.sigla


'''possui chave 1:1 com profile'''

class Conteudo(models.Model):

    usuario = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    titulo = models.CharField(max_length=25)
    imagem = models.CharField(max_length=100)
    tel = models.IntegerField(null=True)
    descricao = models.TextField(max_length=240)
    cep = models.CharField(max_length=8)


    def __str__(self):
        return self.titulo

