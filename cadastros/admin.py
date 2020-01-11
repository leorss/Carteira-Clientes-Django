from django.contrib import admin
from .models import Cliente, Vendedor


class ClienteAdmin(admin.ModelAdmin):
   list_display = ('id', 'cnpj', 'razao_social', 'latitude', 'longitude')
   fieldsets = (
       ('Dados', {
           'fields': ('cnpj', 'razao_social')
       }),
       ('Coordenadas', {
           'fields': (('latitude', 'longitude'))
       }),
   )


class VendedorAdmin(admin.ModelAdmin):
   list_display = ('id', 'cpf', 'razao_social', 'latitude', 'longitude')
   fieldsets = (
       ('Dados', {
           'fields': ('cpf', 'razao_social')
       }),
       ('Coordenadas', {
           'fields': ('latitude', 'longitude')
       }),
   )




admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Vendedor, VendedorAdmin)
