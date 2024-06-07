from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

app_name = 'inventario'  # Asegúrate de que este namespace es único

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),  # Ruta para la vista de inicio
    #path('productos/', include('productos.urls', namespace='productos')),  # Incluye el namespace 'productos'
    path('', include('productos.urls')),  # Incluye las URLs de la aplicación 'productos'
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
