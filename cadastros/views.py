from django.shortcuts import render
from .models import Cliente, Vendedor
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index(request):
    return render(request, 'cadastros/index.html')

def vendedores(request):

    lista = Vendedor.objects.order_by('id')
    paginator = Paginator(lista, 10) # Mostra 25 contatos por página

    # Make sure page request is an int. If not, deliver first page.
    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        lista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista = paginator.page(paginator.num_pages)

    return render(None, 'cadastros/vendedores.html', {"lista":lista})


def clientes(request):

    lista = Cliente.objects.order_by('id')
    paginator = Paginator(lista, 10) # Mostra 25 contatos por página

    # Make sure page request is an int. If not, deliver first page.
    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        lista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista = paginator.page(paginator.num_pages)

    return render(None, 'cadastros/clientes.html', {"lista":lista})
