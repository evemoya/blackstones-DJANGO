
from django.db.models.fields.related import ForeignObject
from django.http import request
from django.shortcuts import render
from .models import Categoria, Corte, Peluquero, Producto, Sucursal


#IMPORTAR EL MODELO DE TABLA  :  LOGIN
from django.contrib.auth.models import User
#IMPORTAR LIBRERIA PARA AUTENTICAR :  LOGIN 
from django.contrib.auth import authenticate, logout, login as login_aut
#IMPORTAR LIBRERIA DECORADORA EVITA INGRESO A PAGINAS SIN AUTORIZACION
from django.contrib.auth.decorators import login_required

# Create your views here.

#ok
def login(request):
    mensaje= ""
    if request.POST:
        nombre = request.POST.get("txtUsuario")
        contra = request.POST.get("txtPass")
        us = authenticate(request,username=nombre, password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            categoria = Categoria.objects.all()
            productos = Producto.objects.filter(portada=True)
            mensaje = "usuario logueado"
            contexto = {"productos":productos,"mensaje":mensaje , "categoria": categoria}
            return render(request, "index.html", contexto)
        else:
            mensaje = "usuario o contrasena incorrecto"
    contexto = {"mensaje":mensaje}
    return render(request, "login.html", contexto)

#ok
def cerrar_sesion(request):
    logout(request)
    productos = Producto.objects.filter(portada=True)
    contexto = {"productos":productos}
    return render(request, "index.html", contexto)

#ok
def index(request):
    categoria = Categoria.objects.all()
    productos = Producto.objects.filter(portada=True)[:5]
    cortes = Corte.objects.filter(publicado=True)[:3]
    contexto = {"productos":productos, "categoria": categoria, "cortes" :cortes}
    return render(request, "index.html", contexto)

#ok
def filtro_categoria(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(publicado=True)
    sucursales = Sucursal.objects.filter(publicado=True)
    peluqueros = Peluquero.objects.filter(publicado=True)
    cortes = Corte.objects.filter(publicado=True)
    cant = Producto.objects.filter(publicado=True).count() + Sucursal.objects.filter(publicado=True).count() + Peluquero.objects.filter(publicado=True).count() + Corte.objects.filter(publicado=True).count()
    if request.POST:
        categoria = request.POST.get("cboCategoria")
        obj_cate = Categoria.objects.get(nombre=categoria)
        productos = Producto.objects.filter(categoria=obj_cate)
        sucursales = Sucursal.objects.filter(categoria=obj_cate)
        peluqueros = Peluquero.objects.filter(categoria=obj_cate)
        cortes = Corte.objects.filter(categoria=obj_cate)
        cant = Producto.objects.filter(categoria=obj_cate).count() + Sucursal.objects.filter(categoria=obj_cate).count() + Peluquero.objects.filter(categoria=obj_cate).count() + Corte.objects.filter(categoria=obj_cate).count()

    contexto = {"productos": productos, "sucursales":sucursales, "peluqueros":peluqueros, "cortes":cortes, "categorias": categorias, "cant":cant}
    return render(request, "galeria.html", contexto)

#ok
def filtro_cate(request, id):
    categorias = Categoria.objects.all()
    obj_cate = Categoria.objects.get(nombre=id)
    sucursales = Sucursal.objects.filter(categoria=obj_cate)
    peluqueros = Peluquero.objects.filter(categoria=obj_cate)
    productos = Producto.objects.filter(categoria=obj_cate)
    cortes = Corte.objects.filter(categoria=obj_cate)
    cant = Producto.objects.filter(categoria=obj_cate).count() or Sucursal.objects.filter(categoria=obj_cate).count() or Peluquero.objects.filter(categoria=obj_cate).count() or Corte.objects.filter(categoria=obj_cate).count()
    contexto = {"sucursales": sucursales, "categorias":categorias, "peluqueros":peluqueros, "productos": productos, "cortes":cortes, "cant":cant}
    return render(request, "galeria.html", contexto)

#error con contador y filtros
def buscar_texto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(publicado=True)
    sucursales = Sucursal.objects.filter(publicado=True)
    peluqueros = Peluquero.objects.filter(publicado=True)
    cortes = Corte.objects.filter(publicado=True)
    #cant = Producto.objects.filter(publicado=True).count() + Sucursal.objects.filter(publicado=True).count() + Peluquero.objects.filter(publicado=True).count() + Corte.objects.filter(publicado=True).count()
    if request.POST:
        texto = request.POST.get("txtTexto")
        productos = Producto.objects.filter(nombre__contains=texto)
        sucursales = Sucursal.objects.filter(nombre__contains=texto) or Sucursal.objects.filter(comuna__contains=texto) or Sucursal.objects.filter(direccion__contains=texto)
        peluqueros = Peluquero.objects.filter(nombre__contains=texto) or Peluquero.objects.filter(descripcion__contains=texto) or  Peluquero.objects.filter(apodo__contains=texto)
        cortes = Corte.objects.filter(nombre__contains=texto)
        #cant = Producto.objects.filter(nombre__contains=texto).count() + Producto.objects.filter(descripcion__contains=texto).count() + Sucursal.objects.filter(nombre__contains=texto).count() + Sucursal.objects.filter(comuna__contains=texto).count() + Sucursal.objects.filter(direccion__contains=texto).count() + Peluquero.objects.filter(nombre__contains=texto).count() + Peluquero.objects.filter(descripcion__contains=texto).count() + Peluquero.objects.filter(apodo__contains=texto).count()
    contexto = {"productos": productos, "peluqueros":peluqueros, "cortes":cortes, "categorias": categorias, "sucursales":sucursales}
    return render(request, "galeria.html", contexto)
 
#ok
def galeria(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(publicado=True)
    sucursales = Sucursal.objects.filter(publicado=True)
    peluqueros = Peluquero.objects.filter(publicado=True)
    cortes = Corte.objects.filter(publicado=True)
    contexto = {"productos": productos, "sucursales":sucursales, "peluqueros":peluqueros, "cortes":cortes, "categorias": categorias}
    return render(request, "galeria.html", contexto)

#Convertir a Formulario
def agendarhora(request):
    return render(request, "agendarhora.html")

#ok
def informaciones(request):
    return render(request, "informaciones.html")

#ok
def tienda(request):
    productos = Producto.objects.filter(publicado=True)
    contexto = {"productos" : productos}
    return render(request, "tienda.html", contexto)

#ok
def ficha(request, id):
    productos = Producto.objects.get(nombre=id)
    contexto = {"productos":productos}
    return render(request, "ficha.html", contexto)

#ok
def barberos(request, id):
    peluquero = Peluquero.objects.get(nombre=id)
    sucursal = Sucursal.objects.all
    cortes = Corte.objects.filter(peluquero=peluquero, publicado = True)
    contexto =  {"peluquero" : peluquero, "sucursal" : sucursal, "cortes":cortes}
    return render(request, "barberos.html", contexto)

#ok
def Quienes_somos(request):
    sucursales = Sucursal.objects.filter(publicado=True)
    contexto = {"sucursales": sucursales}
    return render(request, "Quienes_somos.html", contexto)

#ok
def sucursal(request, id):
    sucursal = Sucursal.objects.get(nombre=id)
    peluqueros = Peluquero.objects.filter(Sucursal=sucursal, publicado = True)
    contexto = {"sucursal": sucursal, "peluqueros": peluqueros}
    return render(request, "sucursal.html", contexto)


@login_required(login_url='/login/')
def administracion(request):
    mensaje=""
    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje}
    return render(request, "administracion.html", contexto)






def registrate(request):
    return render(request, "registrate.html")






##############################
####SITIOS ADMINISTRACION#####
##############################


#ok
@login_required(login_url='/login/')
def eliminar (request, id):
    mensaje=""
    try:
        prod = Producto.objects.get(nombre=id)
        prod.delete()
        mensaje="Se elimino producto"
    except:
        mensaje="no se elimino producto"
    try:
        prod = Peluquero.objects.get(nombre=id)
        prod.delete()
        mensaje="Se elimino Peluquero"
    except:
        mensaje="no se elimino Peluquero"  
    try:
        prod = Sucursal.objects.get(nombre=id)
        prod.delete()
        mensaje="Se elimino Surcusal"
    except:
        mensaje="no se elimino Surcusal"  

    try:
        corte = Corte.objects.get(nombre=id)
        corte.delete()
        mensaje="Se elimino corte"
    except:
        mensaje="no se elimino corte"      


    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje}
    return render(request, "administracion.html", contexto)
   
#ok
@login_required(login_url='/login/')
def modificar(request,id):
    mensaje=""
    print(id)
    try:
        producto = Producto.objects.get(nombre=id)
        categorias = Categoria.objects.all()
        contexto = {"producto":producto, "categorias":categorias}
        return render(request, "modificar_prod.html", contexto)
    except:
        mensaje="no se modifico Producto"

    try:
        sucursal = Sucursal.objects.get(nombre=id)
        categorias = Categoria.objects.all()
        contexto = {"sucursal":sucursal, "categorias":categorias}
        return render(request, "modificar_sucu.html", contexto)
    except:
        mensaje="no se modifico Producto"

    try:
        peluquero = Peluquero.objects.get(nombre=id)
        categorias = Categoria.objects.all()
        sucursales = Sucursal.objects.all()
        contexto = {"peluquero":peluquero, "categorias":categorias,"sucursales":sucursales }
        return render(request, "modificar_pelu.html", contexto)
    except:
        mensaje="no se modifico peluquero"

    try:
        peluquero = Corte.objects.get(nombre=id)
        categorias = Categoria.objects.all()
        peluquero = Peluquero.objects.all()
        contexto = {"peluquero":peluquero, "categorias":categorias,"peluquero":peluquero }
        return render(request, "modificar_corte.html", contexto)
    except:
        mensaje="no se modifico peluquero"

    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje}
    return render(request, "administracion.html", contexto)


@login_required(login_url='/login/')
def modprod(request):
    categorias = Categoria.objects.all()
    contexto = {"categorias" : categorias}
    mensaje=""

    if request.POST:
        nombre = request.POST.get("txtNombre")
        precio = request.POST.get("txtPrecio")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        cate = "productos"
        obj_categoria = Categoria.objects.get(nombre=cate)

        try:
            prod = Producto.objects.get(nombre=nombre)
            prod.precio = precio
            prod.descripcion = desc
            prod.categoria = obj_categoria
            prod.publicado = False
            if foto is not None:
                prod.foto=foto
            prod.save()
            mensaje = "Se modifico Producto " + nombre
        except:
            mensaje = "No modifico producto B"
    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje}

    return render(request, "administracion.html", contexto)

#ok
@login_required(login_url='/login/')
def modsucu(request):
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

        try:
            sucu = Sucursal.objects.get(nombre=nombre)
            sucu.comuna = comuna
            sucu.direccion = direccion
            sucu.telefono = telefono
            sucu.correo = correo
            sucu.horarios = horarios
            sucu.publicado = False
            if foto is not None:
                sucu.foto=foto
            sucu.save()
            mensaje = "Se modifico Sucursal " + nombre
        except:
            mensaje = "No modifico Sucursal"
    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje}

    return render(request, "administracion.html", contexto)

#ok
@login_required(login_url='/login/')
def modpelu(request):
    sucursales = Sucursal.objects.all()
    contexto = {"sucursales" : sucursales}

    if request.POST:
        nombre = request.POST.get("txtNombre")
        apodo = request.POST.get("txtApodo")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        #cate = "peluqueros"
        #obj_categoria = Categoria.objects.get(nombre=cate)
        sucu = request.POST.get("cboSucursales")
        obj_sucursal = Sucursal.objects.get(nombre=sucu)

        try:
            pelu = Peluquero.objects.get(nombre=nombre)
            pelu.apodo = apodo
            pelu.desc = desc
            #pelu.categoria = obj_categoria,
            pelu.Sucursal = obj_sucursal
            if foto is not None:
                pelu.foto=foto
            pelu.save()
            mensaje = "Se modifico Peluquero " + nombre
        except:
            mensaje = "No modifico Peluquero"
    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje}

    return render(request, "administracion.html", contexto)


#ok
@login_required(login_url='/login/')
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

#ok
@login_required(login_url='/login/')
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

#ok
@login_required(login_url='/login/')
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

#ok
def regcorte(request):
    peluqueros = Peluquero.objects.all()
    contexto = {"peluqueros" : peluqueros}

    if request.POST:
        nombre = request.POST.get("txtNombre")
        desc = request.POST.get("txtDesc")
        foto = request.FILES.get("txtImg")
        cate = "Cortes"
        obj_categoria = Categoria.objects.get(nombre=cate)
        pelu = request.POST.get("cboPeluquero")
        obj_pelu = Peluquero.objects.get(nombre=pelu)
        corte = Corte(
            nombre=nombre,
            foto = foto,
            comentario=desc,
            peluquero = obj_pelu,
            categoria = obj_categoria
            )
        corte.save()

        contexto = {"peluqueros" : peluqueros, "mensaje":"Gracias por subir tu corte ya lo publicaremos"} 
    return render(request, "regcorte.html", contexto)

    ##############################




class persona:
    def __init__ (self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


