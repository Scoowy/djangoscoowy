from django.shortcuts import render
from django.utils import timezone
from .models import Post


def listaPost(request):
    posts = Post.objects.filter(
        fechaPublicacion__lte=timezone.now()).order_by('fechaPublicacion')
    return render(request, 'blog/listaPost.html', {'posts': posts})
