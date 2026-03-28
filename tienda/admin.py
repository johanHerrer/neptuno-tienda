from django.contrib import admin
from .models import Producto, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'categoria',
        'precio',
        'descuento',
        'promocion',
        'disponible'
    )

    list_editable = (
        'precio',
        'descuento',
        'promocion',
        'disponible'
    )

    list_filter = ('categoria','promocion')
    search_fields = ('nombre',)