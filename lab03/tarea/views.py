from django.shortcuts import render, get_object_or_404
from .models import Proveedor, Cliente, Producto, Venta, DetalleVenta


# Create your views here.

def index(request):
    return render(request, 'tarea/index.html')

# Vistas para Clientes
def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/listar_clientes.html', {"clientes": clientes})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    telefonos = cliente.telefonos.all()
    return render(request, 'cliente/detalle_cliente.html', {"cliente": cliente, "telefonos": telefonos})

# Vistas para Proveedores
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedor/listar_proveedores.html', {"proveedores": proveedores})

# Vistas para Productos
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/listar_productos.html', {"productos": productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'producto/detalle_producto.html', {"producto": producto})

# Vistas para Ventas
def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'venta/listar_ventas.html', {"ventas": ventas})

def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, id=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)
    return render(request, 'venta/detalle_venta.html', {"venta": venta, "detalles": detalles})
