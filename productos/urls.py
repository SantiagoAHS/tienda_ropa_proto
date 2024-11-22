# productos/urls.py
from django.urls import path
from . import views

app_name = 'productos'  # Esto define el namespace de la app productos

urlpatterns = [
    path('', views.lista_playeras, name='lista_playeras'),
    path('personalizar/<int:playera_id>/', views.personalizar_playera, name='personalizar_playera'),
    path('gestion-playeras/', views.gestionar_playeras, name='gestion_playeras'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('admin/pedidos/', views.lista_pedidos_admin, name='lista_pedidos_admin'),
    path('admin/pedido/<int:pedido_id>/actualizar_estado/', views.actualizar_estado_pedido, name='actualizar_estado_pedido'),
    path('detalles/<int:pedido_id>/', views.detalles_pedido, name='detalles_pedido'),
    # Puedes agregar más URLs aquí, si es necesario
]
