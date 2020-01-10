from django.db import models


class Vendedor(models.Model):
    cpf = models.CharField(max_length=18)
    razao_social = models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=11, decimal_places=0)
    longitude = models.DecimalField(max_digits=11, decimal_places=0)
