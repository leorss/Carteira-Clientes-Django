from django.shortcuts import render

def home(request):
    nome = 'Django MOC'
    return render(request, 'vendedores.html', {'nome': nome})







