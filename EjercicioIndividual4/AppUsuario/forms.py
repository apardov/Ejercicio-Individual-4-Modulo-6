from django.forms import ModelForm

from AppUsuario.models import AppUsuarios


class FormUsuarios(ModelForm):
    class Meta:
        model = AppUsuarios
        fields = '__all__'
