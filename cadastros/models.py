from django.db import models


class Cliente(models.Model):
    cnpj = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=40)
    latitude = models.CharField(max_length=12)
    longitude = models.CharField(max_length=12)
    class Meta:
        db_table = 'Clientes'


class Vendedor(models.Model):
    cpf = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=40)
    latitude = models.CharField(max_length=12)
    longitude = models.CharField(max_length=12)
    class Meta:
        db_table = 'Vendedores'


