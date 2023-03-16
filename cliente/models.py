from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)


    def __str__(self):
        return self.nome + ' ' + self.sobrenome