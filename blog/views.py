from django.shortcuts import render


def listaPost(request):
    return render(request, 'blog/listaPost.html', {})
