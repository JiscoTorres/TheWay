from rest_framework import serializers
from .models import Venda, ItemVenda

class ItemVendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemVenda
        fields = '__all__'
        read_only_fields = ['preco_unitario', 'subtotal']

    def validate_quantidade(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantidade deve ser maior que zero.")
        return value

class VendaSerializer(serializers.ModelSerializer):

    itens = ItemVendaSerializer(many=True)

    class Meta:
        model = Venda
        fields = '__all__'
        read_only_fields = ['data_hora', 'total']

    def validate_itens(self, value):
        if not value:
            raise serializers.ValidationError("A venda deve ter pelo menos um item.")
        return value

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
                venda.delete()
                raise EstoqueInsuficienteException(produto.nome)

            preco_unitario = produto.preco
            subtotal = preco_unitario * quantidade

            ItemVenda.objects.create(
                venda=venda,
                produto=produto,
                quantidade=quantidade,
                preco_unitario=preco_unitario,
                subtotal=subtotal
            )

            produto.qtd_estoque -= quantidade
            produto.save()
            total += subtotal

        venda.total = total
        venda.save()
        return venda
