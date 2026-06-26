import re
from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate_cpf(self, value):
        cpf = re.sub(r'\D', '', value)
        if len(cpf) != 11:
            raise serializers.ValidationError("CPF deve conter 11 dígitos.")
        if cpf == cpf[0] * 11:
            raise serializers.ValidationError("CPF inválido.")
        # Validação dígitos verificadores
        for i in range(9, 11):
            soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(i))
            digito = (soma * 10 % 11) % 10
            if digito != int(cpf[i]):
                raise serializers.ValidationError("CPF inválido.")
        return value

    def validate_telefone(self, value):
        tel = re.sub(r'\D', '', value)
        if len(tel) < 10 or len(tel) > 11:
            raise serializers.ValidationError("Telefone deve conter 10 ou 11 dígitos.")
        return value

    def validate_nome(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Nome deve ter pelo menos 3 caracteres.")
        return value
