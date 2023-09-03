from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('Cursos/', views.cursos, name='Cursos'), 
    path('Profesores/', views.profesores, name='Profesores'),
    path('Suplementos/', views.suplementos, name='Suplementos'),
    path('Asesorados/', views.asesorados, name='Asesorados'),
]



