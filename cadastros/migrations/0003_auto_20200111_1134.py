# Generated by Django 3.0.1 on 2020-01-11 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20200109_2258'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cliente',
            table='Clientes',
        ),
        migrations.AlterModelTable(
            name='vendedor',
            table='Vendedores',
        ),
    ]