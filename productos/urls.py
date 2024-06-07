from django.urls import path 
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Asegúrate de tener una ruta inicial
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('hola-mundo/', views.holaMundo, name='holaMundo'),  # Asegúrate de que esta línea esté presente
    path('home/', views.home, name='home'),
    path('inicio/', views.inicio, name='inicio'),
    
]
