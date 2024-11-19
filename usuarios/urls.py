from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login'),
    path('panel_administrador/', views.panel_administrador, name='panel_administrador'),
    path('panel_cliente/', views.panel_cliente, name='panel_cliente'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


