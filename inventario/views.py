# inventario/views.py

from django.shortcuts import render
from django.http import HttpResponse

def holaMundo(request):
    return HttpResponse("¡Hola, mundo!")

def home(request):
    return render(request, 'home.html')

def inicio(request):
    return render(request, 'inicio.html')