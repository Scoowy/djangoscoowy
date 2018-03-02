from django.contrib import admin
from .models import Post, Comentario


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Datos del Autor', {'fields': ['autor']}),
    ('Datos del Texto', {'fields': ['titulo', 'subtitulo', 'texto']}),
    ('Datos de Fecha', {'fields': ['fechaCreacion', 'fechaPublicacion'], 'classes': ['collapse']}),
    ]
    inlines = [ComentarioInline]
    list_display = ('titulo', 'creado', 'autor', 'isPublicado', 'numeroDiasPublicado')
    list_filter = ['fechaPublicacion', 'fechaCreacion',]
    search_fields = ['^titulo', '^autor',]


admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)
