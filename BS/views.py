from django.shortcuts import render

# Create your views here.

def index(request):
    tipos =  ["asesoria Corte pelo", "Asesoria corte Barba", "Asesoria tratamientos faciales" ]
    contexto = {"nombre" : "NOMBRE APELLIDO", "tipos":tipos}
    return render(request, "index.html", contexto)

def galeria(request):
    return render(request, "galeria.html")


def agendarhora(request):
    return render(request, "agendarhora.html")

def informaciones(request):
    return render(request, "informaciones.html")



    ################################

class persona:
    def __init__ (self, nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


