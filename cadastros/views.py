from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from rest_framework import viewsets
from .models import Cliente, Vendedor
from .forms import ClienteForm, VendedorForm
from cadastros.serializers import ClienteSerializer, VendedorSerializer

import math

def calc_dist(lat1, lon1, lat2, lon2):
	# covert degrees to radians
	lat1 = math.radians(lat1)
	lon1 = math.radians(lon1)
	lat2 = math.radians(lat2)
	lon2 = math.radians(lon2)

	# get the differences
	delta_lat = lat2 - lat1
	delta_lon = lon2 - lon1

	a = ((math.sin(delta_lat/2))**2) + math.cos(lat1)*math.cos(lat2)*((math.sin(delta_lon/2))**2)
	c = 2 * math.atan2(a**0.5, (1-a)**0.5)
	# earth's radius in km
	earth_radius = 6371
	# return distance in miles
	return earth_radius * c


def index(request):
    return render(request, 'cadastros/index.html')


@login_required
def listaCliente(request):
    lista = Cliente.objects.order_by('id')
    query = request.GET.get("q")
    if query:
        lista = lista.filter(
            Q(id__icontains=query) |
            Q(cnpj__icontains=query) |
            Q(razao_social__icontains=query)
            ).distinct()

    paginator = Paginator(lista, 5) # Mostra 5 contatos por página

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

    total = paginator.count
    return render(request, 'cadastros/lista_cliente.html', {"lista":lista, "total": total})


@login_required
def listaVendedor(request):
    lista = Vendedor.objects.order_by('id')

    query = request.GET.get("q")
    if query:
        lista = lista.filter(
            Q(id__icontains=query) |
            Q(cpf__icontains=query) |
            Q(razao_social__icontains=query)
            ).distinct()

    paginator = Paginator(lista, 5) # Mostra 5 contatos por página

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

    total = paginator.count
    return render(request, 'cadastros/lista_vendedor.html', {"lista":lista, "total": total})

@login_required
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


@login_required
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


@login_required
def apagarCliente(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    post.delete()
    return listaCliente(request)


@login_required
def apagarVendedor(request, pk):
    post = get_object_or_404(Vendedor, pk=pk)
    post.delete()
    return listaVendedor(request)


@login_required
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


@login_required
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


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
