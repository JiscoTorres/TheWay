from rest_framework import serializers
from .models import Venda, ItemVenda

class ItemVendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemVenda
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):

    itens = ItemVendaSerializer(many=True)

    class Meta:
        model = Venda
        fields = '__all__'

    def create(self, validated_data):

        itens_data = validated_data.pop('itens')

        venda = Venda.objects.create(**validated_data)

        total = 0

        from produtos.models import Produto
        from core.exceptions import EstoqueInsuficienteException

        for item in itens_data:

            produto = Produto.objects.get(id=item['produto'].id)

            quantidade = item['quantidade']

            if produto.qtd_estoque < quantidade:
                raise EstoqueInsuficienteException()

            subtotal = produto.preco * quantidade

            ItemVenda.objects.create(
                venda=venda,
                produto=produto,
                quantidade=quantidade,
                preco_unitario=produto.preco,
                subtotal=subtotal
            )

            produto.qtd_estoque -= quantidade
            produto.save()

            total += subtotal

        venda.total = total
        venda.save()

        return venda