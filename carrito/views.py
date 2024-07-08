from django.shortcuts import get_object_or_404, redirect
from .carrito import Carrito
from tiendita.models import Producto
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)

    carrito.Agregar(producto=producto)
    return redirect(request.META.get('HTTP_REFERER', 'productos'))

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.eliminar_producto(producto=producto)
    return redirect(request.META.get('HTTP_REFERER', 'productos'))

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    carrito.restar_producto(producto=producto)
    return redirect(request.META.get('HTTP_REFERER', 'productos'))

def limpiar_carrito(request, producto_id):
    carrito = Carrito(request)

    carrito.limpiar_carrito()
    return redirect(request.META.get('HTTP_REFERER', 'productos'))


"""def mostrar_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_carrito = []

    total_carrito = 0

    for producto_id, item in carrito.items():
        producto = Producto.objects.get(id=producto_id)

        productos_carrito.append({
            'producto': producto,
            'imagen_url': producto.imagen.url if producto.imagen else None ,
            'cantidad': item['cantidad'],
        })

    context = {
        'productos_carrito': productos_carrito,
        'total_carrito': total_carrito,
    }

    return render(request, 'carrito.html', context)
"""