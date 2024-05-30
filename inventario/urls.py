"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# inventario/urls.py
from django.contrib import admin
from django.urls import path, include 
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/', views.holaMundo, name='holaMundo'),
    path('', views.home, name='home'),
    path('inicio/', views.inicio, name='inicio'),
    path('productos/', include('productos.urls', namespace='productos')),  # Asegúrate de incluir el namespace
]