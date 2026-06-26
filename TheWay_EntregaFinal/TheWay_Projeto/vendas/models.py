from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

class Venda(models.Model):

    STATUS = [
        ('ABERTA', 'ABERTA'),
        ('CONCLUIDA', 'CONCLUIDA'),
        ('CANCELADA', 'CANCELADA')
    ]

    data_hora = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='CONCLUIDA'
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT
    )

class ItemVenda(models.Model):

    venda = models.ForeignKey(
        Venda,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT
    )

    quantidade = models.IntegerField()

    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )