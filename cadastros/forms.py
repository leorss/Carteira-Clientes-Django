from django import forms
from .models import Cliente
from .models import Vendedor


class AdicionarCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class AdicionarVendedor(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = '__all__'
