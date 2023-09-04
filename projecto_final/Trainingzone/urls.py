from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView
from .views import register





urlpatterns = [  
    path('', login_request, name="login" ),
    #path('login/', login_request, name="login" ),
    #path('', views.home, name='home'),  
    path('Cursos/', views.cursos, name='Cursos'), 
    path('Profesores/', views.profesores, name='Profesores'),
    path('Suplementos/', views.suplementos, name='Suplementos'),
    path('Asesorados/', views.asesorados, name='Asesorados'),
    path('logout/', LogoutView.as_view(template_name="Trainingzone/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('sobremi/', views.sobremi, name="sobremi" ),
]



