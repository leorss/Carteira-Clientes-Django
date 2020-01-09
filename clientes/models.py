from django.db import models


class Cliente(models.Model):
    codigo = models.DecimalField(max_digits=7, decimal_places=0)
    cnpj = models.DecimalField(max_digits=14, decimal_places=0)
    razao_social = models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=11, decimal_places=0)
    longitude = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return self.codigo
