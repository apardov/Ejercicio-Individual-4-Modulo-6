from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class AppUsuarios(models.Model):

    usuario = models.CharField(max_length=100, unique=True, verbose_name='Nombre Usuario')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    telefono = models.CharField(max_length=150, null=True, blank=True, verbose_name='Telefono')
    comuna = models.CharField(max_length=50, null=True, blank=True, verbose_name='Comuna')
    direccion = models.CharField(max_length=50, null=True, blank=True, verbose_name='Direccion')

    def __str__(self):
        return self.usuario

    class Meta:
        verbose_name_plural = 'Usuarios'
        verbose_name = 'Usuario'
