from django.shortcuts import render, redirect
from .models import AppUsuarios
from .forms import FormUsuarios


# Create your views here.

def obtener_usuarios(request):
    usuarios = AppUsuarios.objects.all()
    return render(request, 'base.html', {'usuarios': usuarios})


def crear_usuario(request):
    if request.method == 'POST':
        form = FormUsuarios(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obtener_usuarios')
    else:
        form = FormUsuarios()

    return render(request, 'form.html', {'form': form})
