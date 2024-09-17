# Generated by Django 5.1.1 on 2024-09-17 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=50)),
                ('ano', models.DateField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
            ],
        ),
    ]
