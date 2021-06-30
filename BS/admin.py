from django.contrib import admin
from .models import Categoria, Producto, Sucursal,Peluquero,Corte, Contacto
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Sucursal)
admin.site.register(Peluquero)
admin.site.register(Corte)
admin.site.register(Contacto)

