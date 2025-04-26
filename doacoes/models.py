from django.db import models

# Create your models here.

class Alimento(models.Model):
    nome = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    data_validade = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.quantidade} unidades"

class Roupa(models.Model):
    tipo = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=255)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - Tamanho: {self.tamanho}"

class HigienePessoal(models.Model):
    tipo = models.CharField(max_length=255)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.quantidade} unidades"
