from django.urls import path
from . import views

urlpatterns = [
    
    path('clientes', views.clientes, name='clientes'),
    path('panel', views.panel, name='panel'),
    path('obtener_polizas/<int:id_cliente>/', views.obtener_polizas, name='obtener_polizas'),
    
]