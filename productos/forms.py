# forms.py en la app 'productos'

from django import forms
from .models import Playera

class PlayeraForm(forms.ModelForm):
    class Meta:
        model = Playera
        fields = ['nombre', 'equipo', 'color_principal', 'talla', 'numero_disponibles', 'precio', 'imagen', 'activo']
