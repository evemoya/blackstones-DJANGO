
from django.db.models.fields.related import ForeignObject
from django.shortcuts import render
from .models import Categoria, Peluquero, Producto, Sucursal


# Create your views here.

def index(request):
    tipos =  ["asesoria Corte pelo", "Asesoria corte Barba", "Asesoria tratamientos faciales" ]
    productos = Producto.objects.all()
    contexto = {"nombre" : "NOMBRE APELLIDO", "tipos":tipos, "productos":productos}
    return render(request, "index.html", contexto)

def galeria(request):
    return render(request, "galeria.html")


def agendarhora(request):
    return render(request, "agendarhora.html")

def informaciones(request):
    return render(request, "informaciones.html")

def tienda(request):
    productos = Producto.objects.all()
    contexto = {"productos" : productos}
    return render(request, "tienda.html", contexto)


def Quienes_somos(request):
    return render(request, "Quienes_somos.html")

def sucursal(request):
    return render(request, "sucursal.html")

def sucursal_maipu(request):
    return render(request,"sucursal_maipu.html")

def barberos(request):
    return render(request, "barberos.html")



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


