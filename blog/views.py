from django.shortcuts import render

from .models import *


def listar_publicaciones(request):
    news = Publicacion.objects.all().order_by('-f_pub')
    return render(request, './post/index.html', {'news':news})

def ver_publicacion(request, pub):
    publicacion = Publicacion.objects.get(id = pub)
    return render(request, './post/ver.html', {'publicacion':publicacion})

def ver_publicaciones_categoria(request, categoria):
    categoria = Categoria.objects.get(id = categoria)
    return render(request, './post/index.html', {'categoria':categoria})

