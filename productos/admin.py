from django.contrib import admin
from .models import Pedido, Playera, PlayeraPersonalizada

admin.site.register(Playera)
admin.site.register(PlayeraPersonalizada)
admin.site.register(Pedido)
