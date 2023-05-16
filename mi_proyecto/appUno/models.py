from django.db import models

# Create your models here.
class Contacto (models.Model):
    nombre=models.CharField(max_length=30,blank=True)
    apellido=models.CharField(max_length=30)
    cedula=models.CharField(max_length=30)
    email=models.EmailField()

def __str__(self):
    return self.email