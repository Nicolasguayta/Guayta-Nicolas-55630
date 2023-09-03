from django.http import HttpResponse
from django.template import Template, Context

def Bienvenida (request):
    return HttpResponse("Bienvenidos a Training")

def Bienvenida_html (request):
    return HttpResponse("<html><h1> Bienvenidos a </h1></html>!!")    


def bienvenida_template(request):
    miHtml = open("C:/Users/potoc/Desktop/Proyecto-final/projecto_final/projecto_final/plantillas/bienvenido.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    micontexto = Context()
    Documento = plantilla.render(micontexto)
    return HttpResponse()
