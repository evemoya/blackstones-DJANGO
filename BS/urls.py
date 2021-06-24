
#Rutas de Backstoness


from django.contrib import admin
from django.urls import path, include
from .views import  index, galeria,ficha,administracion,cerrar_sesion,  login, agendarhora, informaciones, tienda, regprod, regpelu, regsucu, Quienes_somos, sucursal, barberos


urlpatterns = [
    path ('', index, name='IND'),
    path ('gale/', galeria, name='GALE' ),
    path ('agenda/',agendarhora, name='AGENDARHORA'),
    path ('info/',informaciones, name='INFO'),
    path ('tienda/',tienda, name='TIENDA'),
    path ('ficha/<id>/', ficha, name='FICHA'),
    path ('regprod/',regprod, name='REGPROD'),
    path ('regpelu/',regpelu, name='REGPELU'),
    path ('regsucu/',regsucu, name='REGSUCU'),
    path ('Quiene_somos/', Quienes_somos, name='QUIENESSOMOS'),
    path ('sucursal/<id>/', sucursal, name='SUCURSAL'),
    path ('barberos/<id>/', barberos, name= 'BARBEROS'),
    path ('administracion/', administracion, name= 'ADM'),
    path ('login/', login, name= 'LOGIN'),
    path ('cerrar/', cerrar_sesion, name= 'CERRAR'),

    
    
]    
