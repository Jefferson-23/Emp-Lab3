from django.db import models

# Create your models here.
class Proveedor(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    pagina_web = models.CharField(max_length=200)

class Cliente(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefonos = models.ManyToManyField('Telefono')

class Telefono(models.Model):
    numero = models.CharField(max_length=10)

class Direccion(models.Model):
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

class Producto(models.Model):
    id_producto = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=200)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

class Venta(models.Model):
    numero_factura = models.CharField(max_length=200, unique=True)
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)