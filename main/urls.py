from django.urls import path
from . import views

urlpatterns = [
    path('', views.sorvete_pedido, name='pedido')
]
