
from django.db.models.fields.related import ForeignObject
from django.http import request
from django.shortcuts import render
from .models import Categoria, Peluquero, Producto, Sucursal

#IMPORTAR EL MODELO DE TABLA  :  LOGIN
from django.contrib.auth.models import User

#IMPORTAR LIBRERIA PARA AUTENTICAR :  LOGIN 
from django.contrib.auth import authenticate, logout, login as login_aut

#IMPORTAR LIBRERIA DECORADORA EVITA INGRESO A PAGINAS SIN AUTORIZACION
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    mensaje= ""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=nombre, password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            productos = Producto.objects.filter(portada=True)
            mensaje = "usuario logueado"
            contexto = {"productos":productos,"mensaje":mensaje }
            return render(request, "index.html", contexto)
        else:
            mensaje = "usuario o contrasena incorrecto"
    contexto = {"mensaje":mensaje}
    return render(request, "login.html", contexto)


def cerrar_sesion(request):
    logout(request)
    productos = Producto.objects.filter(portada=True)
    contexto = {"productos":productos}
    return render(request, "index.html", contexto)


def index(request):
    productos = Producto.objects.filter(portada=True)
    contexto = {"productos":productos}
    return render(request, "index.html", contexto)

def galeria(request):
    return render(request, "galeria.html")


def agendarhora(request):
    return render(request, "agendarhora.html")

def informaciones(request):
    return render(request, "informaciones.html")

def tienda(request):
    productos = Producto.objects.filter(publicado=True)
    contexto = {"productos" : productos}
    return render(request, "tienda.html", contexto)


def ficha(request, id):
    productos = Producto.objects.get(nombre=id)
    contexto = {"productos":productos}
    return render(request, "ficha.html", contexto)

def barberos(request, id):
    peluquero = Peluquero.objects.get(nombre=id)
    sucursal = Sucursal.objects.all
    contexto =  {"peluquero" : peluquero, "sucursal" : sucursal}
    return render(request, "barberos.html", contexto)

def Quienes_somos(request):
    sucursales = Sucursal.objects.all()
    contexto = {"sucursales": sucursales}
    return render(request, "Quienes_somos.html", contexto)

def sucursal(request, id):
    sucursal = Sucursal.objects.get(nombre=id)
    peluqueros = Peluquero.objects.filter(Sucursal=sucursal)
    contexto = {"sucursal": sucursal, "peluqueros": peluqueros}
    return render(request, "sucursal.html", contexto)


def administracion(request):
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos}
    return render(request, "administracion.html", contexto)








##############################
##############################


def regprod(request):
    categorias = Categoria.objects.all()
    contexto = {"categorias" : categorias}

    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        cate = "productos"
        obj_categoria = Categoria.objects.get(nombre=cate)

        prod = Producto(
            nombre=nombre,
            precio=precio,
            descripcion=desc,
            foto = foto,
            categoria = obj_categoria
            )
        prod.save()
        contexto = {"categorias" : categorias, "mensaje":"producto grabado"} 

    return render(request, "regprod.html", contexto)



def regsucu(request):
        categorias = Categoria.objects.all()
        contexto = {"categorias" : categorias}

        if request.POST:
            nombre =  request.POST.get("txtNombre")
            comuna = request.POST.get("txtComuna")
            direccion = request.POST.get("txtDireccion")
            telefono = request.POST.get("txtTelefono")
            correo = request.POST.get("txtCorreo")
            horarios = request.POST.get("txtHorario")
            foto = request.FILES.get("txtImg")

            cate = "sucursales"
            obj_categoria = Categoria.objects.get(nombre=cate)

            sucu = Sucursal(
                nombre = nombre,
                comuna = comuna,
                direccion = direccion,
                telefono = telefono,
                foto = foto,
                correo = correo,
                horarios = horarios,
                categoria = obj_categoria
                )
            sucu.save()
            contexto = {"categorias" : categorias, "mensaje":"Sucursal grabada"} 

        return render(request, "regsucu.html", contexto)




def regpelu(request):
    sucursales = Sucursal.objects.all()
    contexto = {"sucursales" : sucursales}

    if request.POST:
        nombre = request.POST.get("txtNombre")
        apodo = request.POST.get("txtApodo")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        cate = "peluqueros"
        obj_categoria = Categoria.objects.get(nombre=cate)
        sucu = request.POST.get("cboSucursales")
        obj_sucursal = Sucursal.objects.get(nombre=sucu)

        pelu = Peluquero(
            nombre=nombre,
            apodo=apodo,
            descripcion=desc,
            foto = foto,
            categoria = obj_categoria,
            Sucursal = obj_sucursal
            )
        pelu.save()
        contexto = {"sucursales" : sucursales, "mensaje":"Peluquero grabado"} 

    return render(request, "regpelu.html", contexto)



    ##############################

class persona:
    def __init__ (self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


