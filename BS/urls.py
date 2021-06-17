
#Rutas de Backstoness


from django.contrib import admin
from django.urls import path, include
from .views import  index, galeria, agendarhora, informaciones, tienda, regprod, regpelu, regsucu, Quienes_somos, sucursal, sucursal_maipu, barberos


urlpatterns = [
    path ('', index, name='IND'),
    path ('gale/', galeria, name='GALE' ),
    path ('agenda/',agendarhora, name='AGENDARHORA'),
    path ('info/',informaciones, name='INFO'),
    path ('tienda/',tienda, name='TIENDA'),
    path ('regprod/',regprod, name='REGPROD'),
    path ('regpelu/',regpelu, name='REGPELU'),
    path ('regsucu/',regsucu, name='REGSUCU'),
    path ('Quiene_somos/', Quienes_somos, name='QUIENESSOMOS'),
    path ('sucursal/', sucursal, name='SUCURSAL'),
    path ('sucursal_maipu/' ,sucursal_maipu, name='SUCU_MAIPU'),
    path ('barberos/', barberos, name= 'BARBEROS'),
    
    
]    
