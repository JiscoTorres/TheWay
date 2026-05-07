from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('produtos.urls')),
    path('', include('clientes.urls')),
    path('', include('vendas.urls')),
    path('suplementos/', include('suplementos.urls')),
]