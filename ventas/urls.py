from django.urls import path
from . import views

urlpatterns = [
    # Marcas
    path('marcas/', views.MarcaListView.as_view(), name='marca_list'),
    path('marcas/nueva/', views.MarcaCreateView.as_view(), name='marca_create'),
    
    # Modelos
    path('modelos/', views.ModeloListView.as_view(), name='modelo_list'),
    path('modelos/nuevo/', views.ModeloCreateView.as_view(), name='modelo_create'),
    
    # Vendedores
    path('vendedores/', views.VendedorListView.as_view(), name='vendedor_list'),
    path('vendedores/nuevo/', views.VendedorCreateView.as_view(), name='vendedor_create'),
    
    # Clientes
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/nuevo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    
    # Ventas
    path('ventas/', views.VentaListView.as_view(), name='venta_list'),
    path('ventas/nueva/', views.VentaCreateView.as_view(), name='venta_create'),
    
    # Página principal
    path('', views.HomeView.as_view(), name='home'),
]

