from django.conf.urls import url
from rest_framework import urlpatterns 
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

import api

# 'r^  /$'  Definicion de ruta para API

urlpatterns =[
    url(r'^api/productos/$',views.ProductoViewSet.as_view()),
    url(r'^api/productos_portada/$',views.ProductoPortadaViewSet.as_view()),
    url(r'^api/productos_crear/$',views.ProductoCreaterViewSet.as_view()),
    url(r'^api/productos/(?P<nombre>.+)$',views.ProductoBuscarViewSet.as_view()),
    url(r'^api/peluqueros/$',views.PeluqueroViewSet.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)