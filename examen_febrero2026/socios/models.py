from django.db import models
from publicaciones.models import Autor, Publicacion
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class AutorPublicacion(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='autor_publicaciones')
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='autor_publicaciones')

class Video(models.Model):
    TIPO_FORMATO = [
            ('VHS', 'VHS'),
            ('CD', 'CD'),
            ('DVD', 'DVD'),
    ]
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    formato = models.CharField(max_length=20, choices=TIPO_FORMATO)
    año = models.IntegerField(validators=[MinValueValidator(1500), MaxValueValidator(2100)])
    duracion_minutos = models.IntegerField(validators=[MinValueValidator(1)])
    genero = models.CharField(max_length=100)
    sinopsis = models.TextField()

class Disco(models.Model):
    TIPO_FORMATO = [
            ('Vinilo', 'Vinilo'),
            ('CD', 'CD'),
            ('Cassette', 'Cassette'),
    ]
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    formato = models.CharField(max_length=20, choices=TIPO_FORMATO)
    año = models.IntegerField(validators=[MinValueValidator(1500), MaxValueValidator(2100)])
    discografica = models.CharField(max_length=200)
    num_pistas = models.IntegerField(validators=[MinValueValidator(1)])
    genero = models.CharField(max_length=100)

class AutorVideo(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='videos')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='autores')
    rol = models.CharField(max_length=50)

class AutorDisco(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='discos')
    disco = models.ForeignKey(Disco, on_delete=models.CASCADE, related_name='autores')
    rol = models.CharField(max_length=50)