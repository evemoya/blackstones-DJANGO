
#Rutas de Backstoness


from django.contrib import admin
from django.urls import path, include
from .views import  index, galeria,ficha,administracion,cerrar_sesion,filtro_cate, registrate ,filtro_categoria, buscar_texto,  login, agendarhora, informaciones, tienda, regprod, regpelu, regsucu,regcorte, Quienes_somos, sucursal, barberos


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
    path ('sucursal/<id>/', sucursal, name='SUCURSAL'),
    path ('ficha/<id>/', ficha, name='FICHA'),
    path ('barberos/<id>/', barberos, name= 'BARBEROS'),


    #administracion
    path ('administracion/', administracion, name= 'ADM'),
    path ('regprod/',regprod, name='REGPROD'),
    path ('regpelu/',regpelu, name='REGPELU'),
    path ('regsucu/',regsucu, name='REGSUCU'),

    #accesos
    path ('login/', login, name= 'LOGIN'),
    path ('cerrar/', cerrar_sesion, name= 'CERRAR'),
    path ('filtro_cate/<id>', filtro_cate, name= 'FILTROCATE'),
    path ('registrate', registrate, name= 'REGISTRATE'),

    #Filtros
    path ('filtro_categoria/', filtro_categoria, name= 'FILTROCATEGORIA'), 
    path ('buscar_texto/', buscar_texto, name= 'BUSCARTXT'), 
    path ('filtro_cate/<id>', filtro_cate, name= 'FILTROCATE'),


    
    
]    
