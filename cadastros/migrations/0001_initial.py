# Generated by Django 3.0.1 on 2020-01-10 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=18)),
                ('razao_social', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(decimal_places=0, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=18)),
                ('razao_social', models.CharField(max_length=40)),
                ('latitude', models.DecimalField(decimal_places=0, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=0, max_digits=11)),
            ],
        ),
    ]
