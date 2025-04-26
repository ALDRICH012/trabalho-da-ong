from django.db import models

class Alimento(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    data_validade = models.DateField()

class Roupa(models.Model):
    tipo = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=255)
    quantidade = models.IntegerField()

class HigienePessoal(models.Model):
    tipo = models.CharField(max_length=255)
    quantidade = models.IntegerField()