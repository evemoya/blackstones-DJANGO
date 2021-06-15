
#Rutas de Backstones


from django.contrib import admin
from django.urls import path, include
from .views import index, galeria, agendarhora, informaciones

urlpatterns = [
    path ('', index, name='IND'),
    path ('gale/', galeria, name='GALE' ),
    path ('agenda/',agendarhora, name='AGENDARHORA'),
    path ('info/',informaciones, name='INFO'),
    
    
]    