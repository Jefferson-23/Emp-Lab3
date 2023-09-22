from django.contrib import admin
from .models import Proveedor, Cliente, Telefono, Direccion, Producto, Categoria, Venta, DetalleVenta

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Telefono)
admin.site.register(Direccion)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Venta)
admin.site.register(DetalleVenta)
