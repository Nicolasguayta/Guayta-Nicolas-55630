from django.db import models

# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=50)

class Asesorados(models.Model):
    nombre = models.CharField(max_length=50)
    Curso = models.IntegerField() 
    Email = models.EmailField()

class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    Email = models.EmailField()

class Suplementos(models.Model):
    nombre = models.CharField(max_length=50)
    Clase_de_suplemento = models.IntegerField()          