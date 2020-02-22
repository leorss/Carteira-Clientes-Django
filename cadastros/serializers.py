from rest_framework import serializers
from .models import Vendedor, Cliente

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('cnpj', 'razao_social', 'latitude', 'longitude')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ('cpf', 'razao_social', 'latitude', 'longitude')
