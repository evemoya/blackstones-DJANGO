
from django.db.models.fields.related import ForeignObject
from django.http import request
from django.shortcuts import render
from .models import Categoria, Corte, Peluquero, Producto, Sucursal, Contacto

#IMPORTAR EL MODELO DE TABLA  :  LOGIN
from django.contrib.auth.models import User
#IMPORTAR LIBRERIA PARA AUTENTICAR :  LOGIN 
from django.contrib.auth import authenticate, logout, login as login_aut
#IMPORTAR LIBRERIA DECORADORA EVITA INGRESO A PAGINAS SIN AUTORIZACION
from django.contrib.auth.decorators import login_required, permission_required


import requests
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
            cortes = Corte.objects.filter(publicado=True)[:3]
            mensaje = "usuario logueado"
            contexto = {"productos":productos,"mensaje":mensaje , "categoria": categoria, "cortes":cortes}
            return render(request, "index.html", contexto)
        else:
            mensaje = "usuario o contrasena incorrecto"
    contexto = {"mensaje":mensaje}
    return render(request, "login.html", contexto)

#ok
def cerrar_sesion(request):
    logout(request)
    productos = Producto.objects.filter(portada=True)
    categoria = Categoria.objects.all()
    cortes = Corte.objects.filter(publicado=True)[:3]
    mensaje = "usuario logueado"
    contexto = {"productos":productos,"mensaje":mensaje , "categoria": categoria, "cortes":cortes}
    return render(request, "index.html", contexto)

#ok
def index(request):
    categoria = Categoria.objects.all()
    productos = Producto.objects.filter(portada=True)[:3]
    cortes = Corte.objects.filter(publicado=True)[:3]
    contexto = {"productos":productos, "categoria": categoria, "cortes" :cortes}
    #Consumo API 
    response = requests.get('http://127.0.0.1:8000/api/productos/')
    productosAPI = response.json()
    contexto["productosAPI"] = productosAPI
    #Fin Consumo API
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
        productos = Producto.objects.filter(categoria=obj_cate, publicado = True)
        sucursales = Sucursal.objects.filter(categoria=obj_cate, publicado = True)
        peluqueros = Peluquero.objects.filter(categoria=obj_cate, publicado = True)
        cortes = Corte.objects.filter(categoria=obj_cate, publicado = True)
        cant = Producto.objects.filter(categoria=obj_cate,publicado=True).count() + Sucursal.objects.filter(categoria=obj_cate, publicado=True).count() + Peluquero.objects.filter(categoria=obj_cate, publicado=True).count() + Corte.objects.filter(categoria=obj_cate, publicado=True).count()

    contexto = {"productos": productos, "sucursales":sucursales, "peluqueros":peluqueros, "cortes":cortes, "categorias": categorias, "cant":cant}
    return render(request, "galeria.html", contexto)

#ok
def filtro_cate(request, id):
    categorias = Categoria.objects.all()
    obj_cate = Categoria.objects.get(nombre=id)
    sucursales = Sucursal.objects.filter(categoria=obj_cate,publicado=True)
    peluqueros = Peluquero.objects.filter(categoria=obj_cate,publicado=True)
    productos = Producto.objects.filter(categoria=obj_cate,publicado=True)
    cortes = Corte.objects.filter(categoria=obj_cate,publicado=True)
    cant = Producto.objects.filter(categoria=obj_cate,publicado=True).count() or Sucursal.objects.filter(categoria=obj_cate,publicado=True).count() or Peluquero.objects.filter(categoria=obj_cate,publicado=True).count() or Corte.objects.filter(categoria=obj_cate,publicado=True).count()
    contexto = {"sucursales": sucursales, "categorias":categorias, "peluqueros":peluqueros, "productos": productos, "cortes":cortes, "cant":cant}
    return render(request, "galeria.html", contexto)

#OK
def buscar_texto(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(publicado=True)
    sucursales = Sucursal.objects.filter(publicado=True)
    peluqueros = Peluquero.objects.filter(publicado=True)
    cortes = Corte.objects.filter(publicado=True)
    #cant = Producto.objects.filter(publicado=True).count() + Sucursal.objects.filter(publicado=True).count() + Peluquero.objects.filter(publicado=True).count() + Corte.objects.filter(publicado=True).count()
        
    if request.POST:
        texto = request.POST.get("txtTexto")
        productos = Producto.objects.filter(nombre__contains=texto,publicado=True) or Producto.objects.filter(descripcion__contains=texto,publicado=True)
        sucursales = Sucursal.objects.filter(nombre__contains=texto,publicado=True) or Sucursal.objects.filter(comuna__contains=texto,publicado=True) or Sucursal.objects.filter(direccion__contains=texto,publicado=True) or Sucursal.objects.filter(correo__contains=texto,publicado=True)
        peluqueros = Peluquero.objects.filter(nombre__contains=texto,publicado=True) or Peluquero.objects.filter(descripcion__contains=texto,publicado=True) or  Peluquero.objects.filter(apodo__contains=texto,publicado=True)
        cortes = Corte.objects.filter(nombre__contains=texto,publicado=True)
        #cant = Producto.objects.filter(nombre__contains=texto).count() + Producto.objects.filter(descripcion__contains=texto).count() + Sucursal.objects.filter(nombre__contains=texto).count() + Sucursal.objects.filter(comuna__contains=texto).count() + Sucursal.objects.filter(direccion__contains=texto).count() + Peluquero.objects.filter(nombre__contains=texto).count() + Peluquero.objects.filter(descripcion__contains=texto).count() + Peluquero.objects.filter(apodo__contains=texto).count()
        #cantprod = Producto.objects.filter(descripcion__contains=texto,publicado=True).count()
        #cantsucu = Sucursal.objects.filter(nombre__contains=texto,publicado=True).count() + Sucursal.objects.filter(comuna__contains=texto,publicado=True).count() + Sucursal.objects.filter(direccion__contains=texto,publicado=True).count() + Sucursal.objects.filter(correo__contains=texto,publicado=True).count()
        #cantpelu = Peluquero.objects.filter(nombre__contains=texto,publicado=True).count() + Peluquero.objects.filter(descripcion__contains=texto,publicado=True).count() + Peluquero.objects.filter(apodo__contains=texto,publicado=True).count()
        #cant = cantprod + cantsucu + cantpelu
        contexto = {"productos": productos, "peluqueros":peluqueros, "cortes":cortes, "categorias": categorias, "sucursales":sucursales}
        return render(request, "galeria.html", contexto)
    
    
    else:
        categorias = Categoria.objects.all()
        productos = Producto.objects.filter(publicado=True)
        sucursales = Sucursal.objects.filter(publicado=True)
        peluqueros = Peluquero.objects.filter(publicado=True)
        cortes = Corte.objects.filter(publicado=True)
        contexto = {"productos": productos, "peluqueros":peluqueros, "cortes":cortes, "categorias": categorias, "sucursales":sucursales}
        return render(request, "galeria.html", contexto)

#OK
def contactanos(request):
    comentario = Contacto.objects.all()
    formulario = {"comentario" : comentario}

    if request.POST:
        nombre = request.POST.get("textNombre")
        apellido = request.POST.get("textApellido")
        correo = request.POST.get("txtEmail")
        coment = request.POST.get("comentario")
        contacto = Contacto(
            nombre=nombre,
            apellido = apellido,
            correo=correo,
            comentario = coment,
            )
        contacto.save()

        formulario = {"comentario" : comentario, "mensaje":"Gracias, Nos contactaremos con usted a la brevedad"} 
    return render(request, 'contactanos.html', formulario)

#ok
def galeria(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.filter(publicado=True)
    sucursales = Sucursal.objects.filter(publicado=True)
    peluqueros = Peluquero.objects.filter(publicado=True)
    cortes = Corte.objects.filter(publicado=True)
    cant = Producto.objects.filter(publicado=True).count() + Sucursal.objects.filter(publicado=True).count() + Peluquero.objects.filter(publicado=True).count() + Corte.objects.filter(publicado=True).count()
    contexto = {"productos": productos, "sucursales":sucursales, "peluqueros":peluqueros, "cortes":cortes, "categorias": categorias , "cant":cant}
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

#OK
def ficha(request, id):
    productos = Producto.objects.get(nombre=id)
    contexto = {"productos":productos}
    return render(request, "ficha.html", contexto)

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

#ok
def barberos(request, id):
    peluquero = Peluquero.objects.get(nombre=id)
    sucursal = Sucursal.objects.all
    cortes = Corte.objects.filter(peluquero=peluquero, publicado = True)
    contexto =  {"peluquero" : peluquero, "sucursal" : sucursal, "cortes":cortes}
    return render(request, "barberos.html", contexto)
#ok 
def regcorte(request):
    peluqueros = Peluquero.objects.filter(publicado=True)
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

#ok
def registrate(request):
    mensaje = ""
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        correo = request.POST.get("txtEmail")
        user = request.POST.get("txtUser")
        passw1 = request.POST.get("txtPass1")

        try:
            usu = User.objects.get(username=user)
            mensaje = "usuario ya existe"
        except:
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = correo
            usu.username = user
            usu.set_password(passw1)
            usu.save()
            mensaje= "Usuario Registrado"
    contexto = {"mensaje" : mensaje}
    return render(request, "registrate.html", contexto)





##############################
####SITIOS ADMINISTRACION#####
##############################

#PERMISION DELETE
#ok
@login_required(login_url='/login/')
@permission_required('BS.delete_corte', login_url='/login/')
@permission_required('BS.delete_contacto', login_url='/login/')
@permission_required('BS.delete_peluquero', login_url='/login/')
@permission_required('BS.delete_producto', login_url='/login/')
@permission_required('BS.delete_sucursal', login_url='/login/')
def eliminar (request, id):
    mensaje=""
    try:
        prod = Producto.objects.get(nombre=id)
        prod.delete()
        mensaje="Se elimino producto"
    except:
        mensaje=""
    try:
        prod = Peluquero.objects.get(nombre=id)
        prod.delete()
        mensaje="Se elimino Peluquero"
    except:
        mensaje=""  
    try:
        prod = Sucursal.objects.get(nombre=id)
        prod.delete()
        mensaje="Se elimino Surcusal"
    except:
        mensaje=""  

    try:
        corte = Corte.objects.get(nombre=id)
        corte.delete()
        mensaje="Se elimino corte"
    except:
        mensaje=""  

    try :
        contacto = Contacto.objects.get(nombre=id)
        contacto.delete()
        mensaje="Se elimino Contacto"  
    except:
        mensaje=""  


    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contacto = Contacto.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje, "contacto":contacto}
    return render(request, "administracion.html", contexto)
   

#PERMISION MODIFICAR . CHANGE
#ok
@login_required(login_url='/login/')
@permission_required('BS.change_producto', login_url='/login/')
@permission_required('BS.change_sucursal', login_url='/login/')
@permission_required('BS.change_peluquero', login_url='/login/')
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


    categorias = Categoria.objects.all()
    sucursales = Sucursal.objects.all()
    peluqueros = Peluquero.objects.all()
    productos = Producto.objects.all()
    cortes = Corte.objects.all()
    contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje}
    return render(request, "administracion.html", contexto)


@login_required(login_url='/login/')
@permission_required('BS.change_producto', login_url='/login/')
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
@permission_required('BS.change_sucursal', login_url='/login/')
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
@permission_required('BS.change_peluquero', login_url='/login/')
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



#PERMISION ADD / AGREGAR 
#ok
@login_required(login_url='/login/')
@permission_required('BS.add_sucursal', login_url='/login/')
def regsucu(request):
        usuario_actual = request.user.username
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
                categoria = obj_categoria,
                usuario= usuario_actual
                )
            sucu.save()
            contexto = {"categorias" : categorias, "mensaje":"Sucursal grabada"} 

        return render(request, "regsucu.html", contexto)

#ok
@login_required(login_url='/login/')
@permission_required('BS.add_peluquero', login_url='/login/')
def regpelu(request):
    sucursales = Sucursal.objects.all()
    usuario_actual = request.user.username
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
            Sucursal = obj_sucursal,
            usuario= usuario_actual
            )
        pelu.save()
        contexto = {"sucursales" : sucursales, "mensaje":"Peluquero grabado"} 

    return render(request, "regpelu.html", contexto)

#ok
@login_required(login_url='/login/')
@permission_required('BS.add_producto', login_url='/login/')
def regprod(request):
    categorias = Categoria.objects.all()
    usuario_actual = request.user.username
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
            categoria = obj_categoria,
            usuario= usuario_actual
            )
        prod.save()
        contexto = {"categorias" : categorias, "mensaje":"producto grabado"} 
    return render(request, "regprod.html", contexto)




@login_required(login_url='/login/')
@permission_required('BS.delete_corte', login_url='/login/')
def administracion(request):
    usuario_actual = request.user.username
    if usuario_actual == "admin":
        mensaje=""
        categorias = Categoria.objects.all()
        sucursales = Sucursal.objects.all()
        peluqueros = Peluquero.objects.all()
        productos = Producto.objects.all()
        cortes = Corte.objects.all()
        contacto = Contacto.objects.all()
        cantproductos = Producto.objects.filter(usuario=usuario_actual).count()
        cantpeluqueros = Peluquero.objects.filter(usuario=usuario_actual).count() 
        cantsucursales = Sucursal.objects.filter(usuario=usuario_actual).count() 
        contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje, "usuario_actual":usuario_actual, "contacto":contacto, "cantproductos":cantproductos, "cantsucursales":cantsucursales, "cantpeluqueros":cantpeluqueros}
        #Consumo API 1 
        response = requests.get('http://127.0.0.1:8000/api/productos/')
        productosAPI = response.json()
        contexto["productosAPI"] = productosAPI


        response = requests.get('http://127.0.0.1:8000/api/peluqueros/')
        peluquerosAPI = response.json()
        contexto["peluquerosAPI"] = peluquerosAPI

        response = requests.get('http://127.0.0.1:8000/api/productos_portada/')
        productoPortadaAPI = response.json()
        contexto["productoPortadaAPI"] = productoPortadaAPI


        #Fin Consumo API
        return render(request, "administracion.html", contexto)
   
    else:
        
        mensaje=""
        categorias = Categoria.objects.all()
        sucursales = Sucursal.objects.filter(usuario=usuario_actual)
        peluqueros = Peluquero.objects.filter(usuario=usuario_actual)
        productos = Producto.objects.filter(usuario=usuario_actual)
        cortes = Corte.objects.all()
        contacto = Contacto.objects.all()
        cantproductos = Producto.objects.filter(usuario=usuario_actual).count()
        cantpeluqueros = Peluquero.objects.filter(usuario=usuario_actual).count() 
        cantsucursales = Sucursal.objects.filter(usuario=usuario_actual).count() 
        contexto = {"sucursales": sucursales, "peluqueros": peluqueros, "productos": productos, "cortes": cortes, "categorias":categorias, "mensaje":mensaje, "contacto":contacto, "usuario_actual":usuario_actual, "cantproductos":cantproductos, "cantsucursales":cantsucursales, "cantpeluqueros":cantpeluqueros}
        return render(request, "administracion.html", contexto)


    ##############################








