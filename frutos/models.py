from django.db import models
from datetime import datetime

class Familia(models.Model):
    
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    TIPO = (
        ('M','Membro'),
        ('V','Visitante')
    )

    SEXO = (
        ('M','Masculino'),
        ('F','Feminino')
    )
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=14, blank=True, null=True)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateField(null=True)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False, default='V')
    observacao = models.CharField(max_length=150, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, blank=False, null=False, default='M')
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Reuniao(models.Model):
    TIPO = (
        ('P','Partir do Pão'),
        ('M','Ministerial')
    )
    data_reuniao = models.DateField()
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False, default='P')

    def __str__(self):
        return self.tipo + ': ' + self.data_reuniao.strftime("%d %b %Y")

class Frequencia(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    reuniao = models.ForeignKey(Reuniao, on_delete=models.CASCADE)

