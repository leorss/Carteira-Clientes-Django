from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from django.core.paginator import EmptyPage

from .models import Cliente
from .models import Vendedor
from .forms import AdicionarCliente
from .forms import AdicionarVendedor

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

    return render(request, 'cadastros/detalhe_clientes.html', context={'detalhe': detalhe})

def VendedorDetalhe(request, pk):
    try:
        detalhe = Vendedor.objects.get(pk=pk)
    except Cliente.DoesNotExist:
        raise Http404('Id inválido')

    return render(request, 'cadastros/detalhe_vendedores.html', context={'detalhe': detalhe})

def adicionarCliente(request):
    form = AdicionarCliente()

    if request.method == "POST":
        form = AdicionarCliente(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return Clientes(request)
        else:
            print('Erro ao adicionar cliente')

    return render(request,'cadastros/adicionar_cliente.html',{'form':form})


def adicionarVendedor(request):
    form = AdicionarVendedor()

    if request.method == "POST":
        form = AdicionarVendedor(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return Vendedores(request)
        else:
            print('Erro ao adicionar vendedor')

    return render(request,'cadastros/adicionar_vendedor.html',{'form':form})

def apagarCliente(request, pk):
    post = get_object_or_404(Clientes, pk=id)
    post.delete()
    return Clientes(request)

def apagarVendedor(request, pk):
    post = get_object_or_404(Vendedores, pk=id)
    post.delete()
    return Vendedores(request)

def editalCliente(Cliente, id):
    post = get_object_or_404(Cliente, pk=id)
    post.delete()
    return redirect('blog:post_list')