from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'

    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("Preço deve ser maior que zero.")
        return value

    def validate_qtd_estoque(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantidade em estoque não pode ser negativa.")
        return value

    def validate_nome(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Nome do produto deve ter pelo menos 2 caracteres.")
        return value
