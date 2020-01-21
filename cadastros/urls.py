from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('clientes/', views.Clientes, name='clientes'),
    path('vendedores/', views.Vendedores, name='vendedores'),
    path('clientes/<int:pk>/', views.ClienteDetalhe, name='detalhe-cliente'),
    path('vendedores/<int:pk>/', views.VendedorDetalhe, name='detalhe-vendedor'),
    path('clientes/adicionar/', views.adicionarCliente, name='adicionar-cliente'),
    path('vendedores/adicionar/', views.adicionarVendedor, name='adicionar-vendedor'),
    path('clientes/apagar/<int:pk>/', views.apagarCliente, name='apagar-cliente'),
    path('vendedores/apagar/<int:pk>/', views.apagarVendedor, name='apagar-vendedor'),
]
