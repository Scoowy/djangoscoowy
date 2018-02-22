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

    def __str__(self):
        return self.titulo
