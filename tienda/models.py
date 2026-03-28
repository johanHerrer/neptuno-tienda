from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
        null=True,
    )

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/')
    disponible = models.BooleanField(default=True)
    promocion = models.BooleanField(default=False)

    creado = models.DateTimeField(auto_now_add=True)

    def precio_con_descuento(self):
        if self.descuento > 0:
            return self.precio - (self.precio * self.descuento / 100)
        return self.precio

    def __str__(self):
        return self.nombre