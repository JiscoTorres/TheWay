from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Venda
from .serializers import VendaSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all().order_by('-data_hora')
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]
