from django.contrib import admin
from .models import Categoria
from .models import Producto

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields= ("creado", "editado")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields= ("creado", "editado")



admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)

