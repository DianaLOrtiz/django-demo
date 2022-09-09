from calendar import c
from pyexpat import model
from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    fecha_registro = models.DateField()
    activo = models.BooleanField()
    usuario = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)