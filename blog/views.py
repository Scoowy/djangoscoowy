from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Post
from .forms import ContactanosForm


def lista_post(request):
    # fechaPublicacion devuelve mas antigua
    # -fechaPublicacion devuelve mas actual
    posts = Post.objects.filter(
        fechaPublicacion__lte=timezone.now()).order_by('-fechaPublicacion')
    return render(request, 'blog/lista_post.html', {'posts': posts})


def post_completo(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_completo.html', {'post': post})


def contactanos(request):
    if request.method == 'POST':
        form = ContactanosForm(request.POST)
    else:
        form = ContactanosForm()
    return render_to_response('blog/contactanos.html', {'form': form})
