from decimal import Decimal
from .models import PlayeraPersonalizada

class PlayeraPersonalizadaBuilder:
    def __init__(self):
        self.playera_personalizada = PlayeraPersonalizada()

    def set_nombre(self, nombre):
        self.playera_personalizada.nombre_personalizado = nombre
        return self

    def set_numero(self, numero):
        self.playera_personalizada.numero_personalizado = numero
        return self

    def set_color(self, color):
        self.playera_personalizada.color_personalizado = color
        return self

    def set_equipo(self, equipo):
        self.playera_personalizada.equipo = equipo
        return self

    def set_escudo(self, escudo):
        self.playera_personalizada.escudo = escudo
        return self

    def build(self):
        # Calculamos el precio de la playera personalizada antes de devolverla
        # Aquí puedes usar el precio base o cualquier otra lógica que desees
        # Supongamos que el precio base es de 100 y le sumamos un 20% para personalización
        precio_base = Decimal(100)  # Precio base ejemplo
        precio_personalizado = precio_base * Decimal(1.20)  # Se incrementa un 20% por la personalización

        # Asignamos el precio calculado a la playera personalizada
        self.playera_personalizada.precio = precio_personalizado

        return self.playera_personalizada


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construir_playera_personalizada(self, nombre, numero, color, equipo, escudo):
        # Llamamos a todos los métodos del builder para construir la playera personalizada
        return self.builder.set_nombre(nombre).set_numero(numero).set_color(color).set_equipo(equipo).set_escudo(escudo).build()
    
    
