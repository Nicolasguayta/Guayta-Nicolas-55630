from django.shortcuts import render
from .models import Cursos
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import RegistroUsuariosForm


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

def sobremi(request):
    return render(request, "Trainingzone/sobremi.html")       


def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)
                return render(request, "Trainingzone/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "Trainingzone/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "Trainingzone/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "Trainingzone/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "Trainingzone/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "Trainingzone/registro.html", {"form":miForm})     