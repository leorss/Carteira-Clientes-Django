from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('cliente/', views.listaCliente, name='lista-cliente'),
    path('vendedor/', views.listaVendedor, name='lista-vendedor'),
    path('cliente/adicionar/', views.adicionarCliente, name='adicionar-cliente'),
    path('vendedor/adicionar/', views.adicionarVendedor, name='adicionar-vendedor'),
    path('cliente/editar/<int:pk>/', views.editarCliente, name='editar-cliente'),
    path('vendedor/editar/<int:pk>/', views.editarVendedor, name='editar-vendedor'),
    path('cliente/apagar/<int:pk>/', views.apagarCliente, name='apagar-cliente'),
    path('vendedor/apagar/<int:pk>/', views.apagarVendedor, name='apagar-vendedor'),
]
