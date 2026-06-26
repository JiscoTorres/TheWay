from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # API REST
    path('api/', include('produtos.urls')),
    path('api/', include('clientes.urls')),
    path('api/', include('vendas.urls')),

    # Frontend (interface web)
    path('', include('suplementos.urls')),
]
