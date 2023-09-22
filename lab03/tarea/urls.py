from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/<int:venta_id>/', views.detalle_venta, name='detalle_venta'),
]
