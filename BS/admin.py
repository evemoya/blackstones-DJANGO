from django.contrib import admin
from .models import Categoria, Producto, Sucursal,Peluquero
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Peluquero)

