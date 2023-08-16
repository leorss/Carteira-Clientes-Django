import os

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carteira_clientes.settings')

import django

# Import settings
django.setup()

from cadastros.models import Cliente
from cadastros.models import Vendedor
from faker import Faker

fakegen = Faker(['pt-BR'])

def populate_clientes(N=5):
    for entry in range(N):
        fake_nom = fakegen.company()
        fake_cnpj = fakegen.cnpj()
        fake_lat = fakegen.latitude()
        fake_lon = fakegen.longitude()
        Cliente.objects.get_or_create(razao_social=fake_nom, cnpj=fake_cnpj, latitude=fake_lat, longitude=fake_lon)[0]

        print('Cliente: {0} - CNPJ: {1} - Coordenadas: {2}, {3}'.format(fake_nom, fake_cnpj, fake_lat, fake_lon))


def populate_vendedores(N=5):
    for entry in range(N):
        fake_nom = fakegen.name()
        fake_cpf = fakegen.cpf()
        fake_lat = fakegen.latitude()
        fake_lon = fakegen.longitude()
        Vendedor.objects.get_or_create(razao_social=fake_nom, cpf=fake_cpf, latitude=fake_lat, longitude=fake_lon)[0]

        print('Vendedor: {0} - CPF: {1} - Coordenadas: {2}, {3}'.format(fake_nom, fake_cpf, fake_lat, fake_lon))

if __name__ == '__main__':

    print("Populating the databases...Please Wait")

    print("-"*50)
    print("Clientes")
    print("-"*50)

    populate_clientes(100)

    print("-"*50)
    print("Vendedores")
    print("-"*50)

    populate_vendedores(100)

    print('Populating Complete')
