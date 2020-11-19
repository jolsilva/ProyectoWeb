from django.db import models
from .rutificador import validate_rutificador

class Persona(models.Model)  :
    nombre   = models.TextField(max_length=20)
    apellidos = models.TextField(max_length=20)
    rut      = models.TextField(max_length=12, validators=[validate_rutificador])
    sexo     = models.TextField(max_length=10)
    email   = models.TextField(max_length=30)
    contacto = models.TextField(max_length=12)

    def __str__(self)   :
        return self.nombre +" "+ self.apellidos

class Club_Lectores(models.Model):
    numeroTarjeta   = models.TextField(max_length=10)
    saldoDisponible = models.IntegerField()
    rut             = models.TextField(max_length=12, validators=[validate_rutificador])
    clave           = models.TextField(max_length=4)

    def __str__(self) :
        return self.rut + " " + self.numeroTarjeta

