from django.shortcuts import render
from rest_framework import generics #trae paginas web genericas de restframework
from BS.models import Producto, Peluquero
from .serializers import ProductoSerializers, PeluqueroSerializers, Producto_BuscarSerializers, Producto_CrearSerializers

# Create your views here.

class ProductoViewSet(generics.ListAPIView):
    queryset = Producto.objects.filter(publicado=True)
    serializer_class = ProductoSerializers

class ProductoPortadaViewSet(generics.ListAPIView):
    queryset = Producto.objects.filter(portada=True)
    serializer_class = ProductoSerializers

class ProductoCreaterViewSet(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = Producto_CrearSerializers

class ProductoBuscarViewSet(generics.ListAPIView):
    serializer_class = Producto_BuscarSerializers
    def get_queryset(self):
        nombre_producto = self.kwargs['nombre']
        return Producto.objects.filter(nombre=nombre_producto)

class PeluqueroViewSet(generics.ListAPIView):
    queryset = Peluquero.objects.filter(publicado=True)
    serializer_class = PeluqueroSerializers

