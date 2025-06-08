# estoque/models.py (Versão Corrigida)

from django.db import models
from datetime import date # Importamos 'date' para pegar a data atual

# O modelo Produto continua igual
class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    quantidade = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

# Modelo Movimento com o campo ajustado
class Movimento(models.Model):
    TIPO_MOVIMENTO_CHOICES = [
        ('E', 'Entrada'),
        ('S', 'Saída'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    
    # MANTEMOS O NOME, mas trocamos o tipo para DateField
    data_hora = models.DateField()

    data_ultima_movimentacao = models.DateField(
        null=True, 
        blank=True, 
    ) 
    
    tipo = models.CharField(max_length=1, choices=TIPO_MOVIMENTO_CHOICES)

    def __str__(self):
        # Ajustamos a formatação para não buscar a hora
        return f"{self.get_tipo_display()} de {self.quantidade}x {self.produto.nome} em {self.data_hora.strftime('%d/%m/%Y')}"