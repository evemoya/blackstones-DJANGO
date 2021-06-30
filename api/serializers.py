from django.db.models import fields
from rest_framework.utils import model_meta
from BS.models import Producto
from BS.models import Peluquero
from rest_framework import generics, serializers

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "descripcion"] 


class Producto_CrearSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

class Producto_BuscarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"



#Api peluqueros VIEW 
class PeluqueroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Peluquero
        fields = ["nombre", "apodo", "descripcion", "Sucursal"] 

