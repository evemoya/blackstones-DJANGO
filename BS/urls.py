
#Rutas de Backstoness


from django.contrib import admin
from django.urls import path, include
from .views import  index, galeria,ficha,administracion,cerrar_sesion,filtro_cate,eliminar, modificar, registrate ,filtro_categoria, buscar_texto,  login, agendarhora, informaciones, tienda, regprod, regpelu, regsucu,regcorte,modprod,modsucu,modpelu, Quienes_somos, sucursal, barberos


urlpatterns = [

    #contenido
    path ('', index, name='IND'),
    path ('gale/', galeria, name='GALE' ),
    path ('info/',informaciones, name='INFO'),
    path ('tienda/',tienda, name='TIENDA'),
    path ('Quiene_somos/', Quienes_somos, name='QUIENESSOMOS'),
    path ('regcorte/',regcorte, name='REGCORTE'),
    path ('agenda/',agendarhora, name='AGENDARHORA'),

    #contenido / Fichas
    path ('ficha/<id>/', ficha, name='FICHA'),
    path ('sucursal/<id>/', sucursal, name='SUCURSAL'),
    path ('barberos/<id>/', barberos, name= 'BARBEROS'),


    #ADMINISTRACION 
    path ('administracion/', administracion, name= 'ADM'),
    ####PAGINAS DE REGISTRO
    path ('regpelu/',regpelu, name='REGPELU'),
    path ('regsucu/',regsucu, name='REGSUCU'),
    path ('regprod/',regprod, name='REGPROD'),
   
    #PAGINAS DE MODIFICACION 
    path ('modificar_prod/<id>/', modificar, name= 'MODIFICARPROD'),
    path ('modificar_sucu/<id>/', modificar, name= 'MODIFICARSUCU'),
    path ('modificar_pelu/<id>/', modificar, name= 'MODIFICARPELU'),
    path ('modprod/', modprod, name= 'MODPROD'),
    path ('modsucu/', modsucu, name= 'MODSUCU'),
    path ('modpelu/', modpelu, name= 'MODPELU'),
    path ('eliminar/<id>/',eliminar, name='ELIMINAR'),

  
    #ACCESOS
    path ('login/', login, name= 'LOGIN'),
    path ('cerrar/', cerrar_sesion, name= 'CERRAR'),
    path ('registrate', registrate, name= 'REGISTRATE'),

    #Filtros
    path ('filtro_categoria/', filtro_categoria, name= 'FILTROCATEGORIA'), 
    path ('buscar_texto/', buscar_texto, name= 'BUSCARTXT'), 
    path ('filtro_cate/<id>', filtro_cate, name= 'FILTROCATE'),


    
    
]    
