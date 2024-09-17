from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Marca, Carro

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'modelo', 'cor', 'ano', 'marca')