from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='inicio'),

    #PRODUCTO
    path('index.html', views.index, name='index'),

    path('productos.html', views.productos, name='productos'),

    path('nosotros.html', views.nosotros, name='nosotros'),
    path('contacto.html', views.contacto, name='contacto'), 
    path('carrito.html', views.carrito, name='carrito'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)