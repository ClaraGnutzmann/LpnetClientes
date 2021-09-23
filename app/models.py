from django.db import models

class Cliente(models.Model):
    Nome = models.CharField(max_length=30)
    DDD = models.IntegerField(max_length=3)
    Telefone = models.IntegerField(max_length=9)
    Cidade = models.CharField(max_length=30)
    Idade = models.IntegerField(max_length=3)
    Valor = models.FloatField(max_length=10)
