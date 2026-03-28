from django.shortcuts import render
from .models import Producto, Categoria
from django.contrib.admin.views.decorators import staff_member_required

def inicio(request):

    categoria_id = request.GET.get('categoria')
    busqueda = request.GET.get('q')

    productos = Producto.objects.filter(disponible=True)
    categorias = Categoria.objects.all()
    promociones = Producto.objects.filter(promocion=True)

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)

    return render(request, 'index.html', {
        'productos': productos,
        'categorias': categorias,
        'promociones': promociones
    })


@staff_member_required
def dashboard(request):

    total_productos = Producto.objects.count()
    total_categorias = Categoria.objects.count()
    total_promociones = Producto.objects.filter(promocion=True).count()

    productos = Producto.objects.order_by('-creado')[:5]

    return render(request, 'dashboard.html', {
        'total_productos': total_productos,
        'total_categorias': total_categorias,
        'total_promociones': total_promociones,
        'productos': productos
    })