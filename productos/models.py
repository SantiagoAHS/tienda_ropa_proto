from django.db import models

class Playera(models.Model):
    nombre = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    color_principal = models.CharField(max_length=50)
    talla = models.CharField(
        max_length=5, 
        choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')]
    )
    numero_disponibles = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_playeras/', blank=True, null=True)
    activo = models.BooleanField(default=True)  # Define si la playera está activa para edición

    def __str__(self):
        return f"{self.nombre} ({self.equipo}) - {self.color_principal}"


class PlayeraPersonalizada(models.Model):
    playera_base = models.ForeignKey(Playera, on_delete=models.CASCADE, related_name="personalizaciones")
    nombre_personalizado = models.CharField(max_length=100)
    numero_personalizado = models.IntegerField()
    color_personalizado = models.CharField(max_length=7, blank=True, null=True)  # Color en formato hexadecimal
    escudo = models.ImageField(upload_to='escudos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Si la playera base no está activa, no permitimos guardar campos que no son editables
        if not self.playera_base.activo:
            self.color_personalizado = None  # Forzamos a no permitir cambios en el color
            self.escudo = None  # Forzamos a no permitir cambios en el escudo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Playera personalizada de {self.nombre_personalizado} ({self.numero_personalizado})"
    
# models.py
from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    personalizacion = models.ForeignKey(PlayeraPersonalizada, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, default='En espera')  # Estado del pedido: En espera, Completado, etc.
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido de {self.usuario.username} - {self.personalizacion.nombre_personalizado}"
