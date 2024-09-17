from django import forms
from .models import Carro

class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['descricao', 'modelo', 'cor', 'ano', 'marca']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descrição'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Modelo'}),
            'cor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cor'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ano'}),
            'marca': forms.Select(attrs={'class': 'form-select'})
        }
