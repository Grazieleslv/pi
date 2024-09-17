from django.shortcuts import render, redirect, get_object_or_404
from .models import Carro
from .forms import CarroForm

def index(request):
    return render(request, 'core/index.html')

def cadastro(request):
    form = CarroForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('lista')
    return render(request, 'core/form.html', {'form': form})


def lista(request):
    carros = Carro.objects.all()
    return render(request, 'core/lista.html', {'carros': carros})


def atualizar(request, id):
    carro = get_object_or_404(Carro, id=id)
    
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = CarroForm(instance=carro)
    
    return render(request, 'core/form.html', {'form': form, 'carro': carro})


def deletar(request, id):
    carro = Carro.objects.get(id=id)
    if request.method == 'POST':
        carro.delete()
        return redirect('lista')
    return render(request, 'delete_confirm.html', {'carro': carro})
