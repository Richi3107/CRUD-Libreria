from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro
from .forms import Libroform
# aqui se pones los request de la paginas
def inicio(request):
    return render(request,'paginas/inicio.html')
def nosotros(request):
    return render(request,'paginas/nosotros.html')
def libros(request):
    libros=Libro.objects.all()
    # print(libros)
    return render(request,'libros/index.html',{'libros':libros})

def crear(request):
    formulario=Libroform(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('libros')

    return render(request,'libros/crear.html', {'formulario':formulario})
    
def editar(request,id):
    libro=Libro.objects.get(id=id)
    formulario=Libroform(request.POST or None,request.FILES or None,instance=libro)
    if formulario.is_valid() and request.method== 'POST':
        formulario.save()
        return redirect('libros')
    return render(request,'libros/editar.html',{'formulario':formulario})


def mostrar(request):
    return render(request,'libros/index.html')

def eliminar(request,id):
    libro= Libro.objects.get(id=id)
    libro.delete()
    return redirect('libros')
