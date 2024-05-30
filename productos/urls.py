# inventario/urls.py
from django.contrib import admin
from django.urls import path
from productos import views
from .views import holaMundo 
# productos/urls.py

from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/', views.holaMundo, name='holaMundo'),  # Usa 'holaMundo' aquí
    path('', views.home, name='home'),  # Asegúrate de tener definida esta vista también
    path('inicio/', views.inicio, name='inicio'),  # Añade esta línea
    path('', views.lista_productos, name='lista_productos'),
    path('<int:producto_id>/', views.detalle, name='detalle'),
    
]   
