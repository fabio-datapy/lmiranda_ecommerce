from django.db import models
from django.contrib.auth.models import User


class Pedido(models.Models):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    sttaus = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Fianlizado'),
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'
    

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField(max_length=255)
    produto_id = models.PositiveIntegerField()
    variacao_id = models.PositiveIntegerField()
    preco = models.FolatField()
    preco_promocional = models.FloatField(default=0)
    quantidade = models.PositiveBigIntegerField()
    imagem = models.CharField(max_length=20000)

    def __str__(self):
        return f'Item do {self.pedido}'
    
    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
