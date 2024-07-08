from django.db import models
import random
import string
# Create your models here.
class Categoria(models.Model):
    id_cat = models.IntegerField(primary_key=True, default=1)  
    nombre = models.CharField(max_length=50)
    creado = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categoriaS'

    def __str__ (self):
        return self.nombre


def generate_unique_id():
    length = 6  
    letters = string.ascii_letters  # Todas las letras del alfabeto (mayúsculas y minúsculas)
    random_letters = ''.join(random.choice(letters) for i in range(length))
    return f"{length}-{random_letters}"


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    codigo_unico = models.IntegerField(unique=True, default=None)
    descripcion = models.CharField(max_length=1000)
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE)  
    imagen = models.ImageField(upload_to='media', null=True, blank=True)
    precio = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)
    creado = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productoS'

    def __str__(self):
        return self.nombre

    