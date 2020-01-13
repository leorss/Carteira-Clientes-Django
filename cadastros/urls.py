from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('clientes/', views.Clientes, name='clientes'),
    path('vendedores/', views.Vendedores, name='vendedores'),
    path('clientes/<int:pk>', views.ClienteDetalhe, name='cliente-detalhe'),
    path('vendedores/<int:pk>', views.VendedorDetalhe, name='vendedor-detalhe'),
]
