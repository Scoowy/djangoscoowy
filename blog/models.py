import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=100, blank=True, null=True)
    texto = models.TextField()
    fechaCreacion = models.DateTimeField(default=timezone.now)
    fechaPublicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fechaPublicacion = timezone.now()
        self.save()

    def numeroDiasPublicado(self):
        numDias = 0
        if self.fechaPublicacion:
            fechaActual = datetime.now()
            numDias = fechaActual - self.fechaPublicacion
            numDias = numDias.days

            return numDias
        else:
            return numDias

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.TextField(blank=False)
    fechaCreacion = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    def isActivo(self):
        return activo

    def __str__(self):
        return self.titulo
