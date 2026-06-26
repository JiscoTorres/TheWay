from django.urls import path
from . import views

urlpatterns = [
    path('', views.recomendacao_view, name='recomendacao'),
]