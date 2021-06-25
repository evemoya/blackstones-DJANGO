from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=40)
    imagen = models.ImageField(upload_to='media/categoria', null=True)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    foto = models.ImageField(upload_to='media/productos', null=True)
    publicado = models.BooleanField(default=False)
    portada = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero:"+str(self.id_auto_inc)
    
class Sucursal(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50, null=True)
    horarios  = models.CharField(max_length=50, null=True)
    direccion = models.CharField(max_length=100)
    publicado = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='media/sucursal', null=True)
    mapa = models.CharField(max_length=500, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "Numero:"+str(self.id_auto_inc)

class Peluquero(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apodo = models.CharField(max_length=50, null= True)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='media/peluqueros', null=True)
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

class Corte(models.Model):
    id_auto_inc = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='media/cortes', null=True)
    publicado = models.BooleanField(default=False)
    comentario = models.TextField(null=True)
    peluquero = models.ForeignKey(Peluquero, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "Numero:"+str(self.id_auto_inc)