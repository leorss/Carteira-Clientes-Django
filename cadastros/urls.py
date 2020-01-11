from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('vendedores/', views.vendedores, name='vendedores'),
]