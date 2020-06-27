from django.shortcuts import render
from .models import Post
from .models import Integrantes
from .models import Galeria
from .models import ImagenEnGaleria
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
import math
from array import array


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    integrantes= Integrantes.objects.all
    galerias=Galeria.objects.order_by('-pk')[0:3]



    return render(request, 'blog/post_list.html', {"posts":posts, "integrantes":integrantes,"galerias":galerias})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def noticias(request, num):
    n=int(num)
    p=3
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[(n-1)*p:(n-1)*p+(p)]
    total = Post.objects.count()
    ultima=math.ceil(total/p)
    total_array=[]
    print(ultima)
    if num-3<=0:
        for x in range(1,ultima+1):
            total_array.append(x)
    elif num+3>ultima:
        for x in range(ultima-3,ultima+1):
            total_array.append(x)
    else:
        for x in range(ultima-2,ultima+2):
            total_array.append(x)
    print(total_array)
    return render(request, 'blog/noticias.html', {'posts':posts,'num':num,'total_array':total_array })

def galerias(request, num):
    n=int(num)
    p=3
    galerias = Galeria.objects.order_by('-pk')[(n-1)*p:(n-1)*p+(p)]
    total = Galeria.objects.count()
    ultima=math.ceil(total/p)
    total_array=[]

    if num-3<=0:
        for x in range(1,ultima+1):
            total_array.append(x)
    elif num+3>ultima:
        for x in range(ultima-3,ultima+1):
            total_array.append(x)
    else:
        for x in range(ultima-2,ultima+2):
            total_array.append(x)
    return render(request, 'blog/galerias.html', {'galerias':galerias,'num':num,'total_array':total_array })

def galeria(request,pk):
    imagenes=ImagenEnGaleria.objects.filter(galeria=pk)
    nombre=Galeria.objects.filter(pk=pk)
    return render(request, 'blog/galeria.html',{'imagenes':imagenes,'nombre':nombre})
