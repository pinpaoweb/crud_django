from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.http import HttpResponse
from django.contrib import messages

def lista_productos(request):
    productos_list = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos_list})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle.html', {'producto': producto})

def crear_producto(request):
    # Lógica para crear un producto
    return render(request, 'crear_producto.html')

def editar_producto(request, id):
    # Lógica para editar un producto
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'editar_producto.html', {'producto': producto})

def eliminar_producto(request, id):
    # Lógica para eliminar un producto
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, 'El producto ha sido eliminado con éxito.')
    return redirect('productos:lista_productos')

def holaMundo(request):
    return HttpResponse("¡Hola, Mundo ADSO!")

def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')
