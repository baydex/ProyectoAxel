from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user', default=None
    )
    edad = models.SmallIntegerField()
    sexo = models.SmallIntegerField()
    nivel_educativo = models.SmallIntegerField()
    ocupacion = models.SmallIntegerField()
    introvertido_extrovertido = models.SmallIntegerField()
    calmado_nervioso = models.SmallIntegerField()
    mas_importancia = models.SmallIntegerField()
    deporte = models.SmallIntegerField()
    viajar = models.SmallIntegerField()
    videojuegos = models.SmallIntegerField()
    leer = models.SmallIntegerField()
    cine = models.SmallIntegerField()
    amistad = models.SmallIntegerField()
    mascotas = models.SmallIntegerField()
    apariencia = models.SmallIntegerField()
    salud = models.SmallIntegerField()
    experimentar = models.SmallIntegerField()
    hijos = models.SmallIntegerField()
    musica = models.SmallIntegerField()
    sueño = models.SmallIntegerField()