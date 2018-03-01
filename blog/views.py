from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.db.models import Q
from .models import Post
from .forms import ContactanosForm


def index(request):
    return render(request, 'blog/index.html')


def lista_post(request):
    # fechaPublicacion devuelve mas antigua
    # -fechaPublicacion devuelve mas actual
    posts = Post.objects.filter(
        fechaPublicacion__lte=timezone.now()).order_by('-fechaPublicacion')
    return render(request, 'blog/lista_post.html', {'posts': posts})


def post_completo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_completo.html', {'post': post})


def buscar(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(autor__username__icontains=query) |
            Q(titulo__icontains=query) |
            Q(subtitulo__icontains=query)
        )
        resultados = Post.objects.filter(qset).distinct()
    else:
        resultados = []
    numResultados = len(resultados)
    return render_to_response('blog/busqueda.html', {'resultados': resultados, 'query': query, 'numResultados': numResultados})


def contactanos(request):
    if request.method == 'POST':
        form = ContactanosForm(request.POST)
        if form.is_valid():
            topic = form.clean_data['topic']
            mensaje = form.clean_data['mensaje']
            nombre = form.clean_data.get['nombre', 'ANONIMO']
            sender = form.clean_data.get['sender', 'noreply@example.com']
            subject = 'Comentario o sugerencia de ' + nombre + ', tema: ' + topic
            send_mail(
                subject,
                mensaje,
                sender,
                ['gahonajuanjo@gmail.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect('/contactanos/gracias/')
    else:
        form = ContactanosForm()
    return render_to_response('blog/contactanos.html', {'form': form})


def contactanos_gracias(request):
    return render(request, 'blog/contactanos_gracias.html')
