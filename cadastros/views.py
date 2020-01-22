from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import InvalidPage
from django.core.paginator import EmptyPage

from .models import Cliente
from .models import Vendedor
from .forms import ClienteForm
from .forms import VendedorForm


def index(request):
    return render(request, 'cadastros/index.html')


def Http404(request, msg):
    return render(request, 'cadastros/404.html')


def listaVendedor(request):
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

    return render(None, 'cadastros/lista_vendedor.html', {"lista":lista})


def listaCliente(request):
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

    return render(None, 'cadastros/lista_cliente.html', {"lista":lista})


def adicionarCliente(request):
    form = ClienteForm()

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return listaCliente(request)
        else:
            print('Erro ao adicionar cliente')

    return render(request,'cadastros/adicionar_cliente.html',{'form':form})


def adicionarVendedor(request):
    form = VendedorForm()

    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return listaVendedor(request)
        else:
            print('Erro ao adicionar vendedor')

    return render(request,'cadastros/adicionar_vendedor.html',{'form':form})

def apagarCliente(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    post.delete()
    return listaCliente(request)


def apagarVendedor(request, pk):
    post = get_object_or_404(Vendedor, pk=pk)
    post.delete()
    return listaVendedor(request)


def editarCliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(instance=cliente)
    if (request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)

        if (form.is_valid()):
            cliente = form.save(commit=False)
            cliente.cnpj = form.cleaned_data['cnpj']
            cliente.razao_social = form.cleaned_data['razao_social']
            cliente.latitude = form.cleaned_data['latitude']
            cliente.longitude = form.cleaned_data['longitude']
            cliente.save()
            return listaCliente(request)
        else:
            return render(request, 'cadastros/editar_cliente.html', {'form': form, 'cliente': cliente})
    elif (request.method == 'GET'):
        return render(request, 'cadastros/editar_cliente.html', {'form': form, 'cliente': cliente})


def editarVendedor(request, pk):
    vendedor = get_object_or_404(Vendedor, pk=pk)
    form = VendedorForm(instance=vendedor)
    if (request.method == 'POST'):
        form = VendedorForm(request.POST, instance=vendedor)

        if (form.is_valid()):
            vendedor = form.save(commit=False)
            vendedor.cpf = form.cleaned_data['cpf']
            vendedor.razao_social = form.cleaned_data['razao_social']
            vendedor.latitude = form.cleaned_data['latitude']
            vendedor.longitude = form.cleaned_data['longitude']
            vendedor.save()
            return listaVendedor(request)
        else:
            return render(request, 'cadastros/editar_vendedor.html', {'form': form, 'vendedor': vendedor})
    elif (request.method == 'GET'):
        return render(request, 'cadastros/editar_vendedor.html', {'form': form, 'vendedor': vendedor})
