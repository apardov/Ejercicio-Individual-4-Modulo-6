from django.contrib import admin
from django.urls import path

from AppUsuario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.obtener_usuarios, name='obtener_usuarios'),
    path('crearusuario/', views.crear_usuario, name='crear_usuario'),
]
