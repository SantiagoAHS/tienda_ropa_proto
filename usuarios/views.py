# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistroUsuarioForm

from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroUsuarioForm

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def acerca(request):
    return render(request, 'acerca.html')

# Vista para registro de usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignamos automáticamente el grupo "Cliente"
            cliente_group = Group.objects.get(name='Cliente')
            user.groups.add(cliente_group)
            login(request, user)
            return redirect('productos:lista_playeras')  # Redirige a la lista de productos después del registro
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)

            # Identificar el grupo del usuario
            if usuario.groups.filter(name='Administrador').exists():
                request.session['tipo_usuario'] = 'Administrador'
                return redirect('usuarios:panel_administrador')
            else:
                request.session['tipo_usuario'] = 'Cliente'
                return redirect('usuarios:panel_cliente')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login_usuario.html', {'form': form})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vista para el panel del administrador
@login_required
def panel_administrador(request):
    # Solo permitir a los usuarios que son administradores acceder a esta vista
    if request.user.groups.filter(name='Administrador').exists():
        return render(request, 'usuarios/panel_administrador.html')  # Renderiza la plantilla para el administrador
    else:
        return redirect('productos:lista_playeras')  # Redirige a la lista de productos si no es administrador
    

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vista para el panel del cliente
@login_required
def panel_cliente(request):
    # Solo permitir a los usuarios que son clientes acceder a esta vista
    if request.user.groups.filter(name='Cliente').exists():
        return render(request, 'usuarios/panel_cliente.html')  # Renderiza la plantilla para el cliente
    else:
        return redirect('productos:lista_playeras')  # Redirige a la lista de productos si no es cliente
