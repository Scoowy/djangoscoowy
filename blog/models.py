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
            fechaActual = timezone.now()
            numDias = fechaActual - self.fechaPublicacion
            numDias = numDias.days

            return numDias
        else:
            return numDias

    def isPublicado(self):
        if self.fechaPublicacion:
            return True
        else:
            return False

    def propFechaCreacion(self):
        return self.fechaCreacion
    propFechaCreacion.short_description = "Creado el:"
    creado = property(propFechaCreacion)


    def __str__(self):
        return self.titulo

    isPublicado.boolean = True
    isPublicado.short_description = "Publicado"
    numeroDiasPublicado.short_description = "Dias Pub."

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.TextField(blank=False)
    fechaCreacion = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    def desActivar(self):
        if self.activo:
            self.activo = False
            self.save()
        else:
            self.activo = True
            self.save()

    def isActivo(self):
        return activo

    def __str__(self):
        return self.titulo
