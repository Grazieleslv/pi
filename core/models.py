from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Carro(models.Model):
    descricao = models.CharField(max_length=255)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    ano = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo} - {self.descricao}"
