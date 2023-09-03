from django.shortcuts import render
from .models import Cursos


# Create your views here.

def home(request):
    return render(request, "Trainingzone/base.html")

def cursos(request):
    return render(request, "Trainingzone/Cursos.html")

def profesores(request):
    return render(request, "Trainingzone/Profesores.html" )

def suplementos(request):
    return render(request, "Trainingzone/Suplementos.html" )

def asesorados(request):
    return render(request, "Trainingzone/Suplementos.html" )      
