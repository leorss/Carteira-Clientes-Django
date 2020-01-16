from django.shortcuts import render
from .models import Cliente, Vendedor
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def index(request):
    return render(request, 'cadastros/index.html')


def Http404(request, msg):
    return render(request, 'cadastros/404.html')


def Vendedores(request):
    lista = Vendedor.objects.order_by('id')
    paginator = Paginator(lista, 5) # Mostra 25 contatos por página

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


def Clientes(request):
    lista = Cliente.objects.order_by('id')
    paginator = Paginator(lista, 5) # Mostra 25 contatos por página

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


def ClienteDetalhe(request, pk):
    try:
        detalhe = Cliente.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        raise Http404('Id inválido')

    return render(request, 'cadastros/clientes_detalhe.html', context={'detalhe': detalhe})

def VendedorDetalhe(request, pk):
    try:
        detalhe = Vendedor.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        raise Http404('Id inválido')

    return render(request, 'cadastros/vendedores_detalhe.html', context={'detalhe': detalhe})

