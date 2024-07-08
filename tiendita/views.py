from django.shortcuts import render
from .models import Producto
from .models import Categoria
#Vistas de la tiendita 

def index(request):
    return render(request, 'frontend/index.html')

def productos(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, "frontend/productos.html", {"categorias": categorias, "productos": productos})

def nosotros(request):
    return render(request, "frontend/nosotros.html")

def contacto(request):
    return render(request, "frontend/contacto.html")

def carrito(request):
    return render(request, "frontend/carrito.html")

