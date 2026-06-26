from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from .exceptions import EstoqueInsuficienteException

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, EstoqueInsuficienteException):
        msg = f"Estoque insuficiente para o produto: {exc.produto_nome}" if exc.produto_nome else "Estoque insuficiente."
        return Response({'erro': msg}, status=status.HTTP_400_BAD_REQUEST)

    return response
