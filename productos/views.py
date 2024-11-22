# Create your views here.
from django.shortcuts import get_object_or_404, render
from .models import Playera  # Asegúrate de importar el modelo de productos (Playera)
from .builders import PlayeraPersonalizadaBuilder, Director

def lista_playeras(request):
    productos = Playera.objects.all()  # Obtén todos los productos
    return render(request, 'productos/lista_playeras.html', {'productos': productos})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Playera, PlayeraPersonalizada, Pedido
from django.contrib.auth.decorators import login_required

@login_required(login_url='usuarios:login')
def personalizar_playera(request, playera_id):
    playera = get_object_or_404(Playera, id=playera_id)

    if request.method == 'POST':
        nombre_personalizado = request.POST.get('nombre_personalizado')
        numero_personalizado = request.POST.get('numero_personalizado')
        color_personalizado = request.POST.get('color_personalizado', None)  # Opcional
        escudo = request.FILES.get('escudo', None)  # Opcional

        # Creamos o actualizamos la playera personalizada
        playera_personalizada = PlayeraPersonalizada(
            playera_base=playera,
            nombre_personalizado=nombre_personalizado,
            numero_personalizado=numero_personalizado,
        )

        # Si la playera base está activa, permitimos personalizar todos los campos
        if playera.activo:
            playera_personalizada.color_personalizado = color_personalizado
            playera_personalizada.escudo = escudo

        # Guardamos la playera personalizada
        playera_personalizada.save()

        # Guardamos el pedido
        Pedido.objects.create(
            usuario=request.user,
            personalizacion=playera_personalizada,
            estado="En espera"  # Estado inicial del pedido
        )

        # Redirigimos a la lista de pedidos
        return redirect('productos:lista_pedidos')  # Asegúrate de que la URL de lista_pedidos esté bien definida

    return render(request, 'productos/personalizar_playera.html', {'playera': playera})

# views.py en la app 'productos'

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Playera
from .forms import PlayeraForm

def gestionar_playeras(request):
    if request.method == 'POST':
        # Verificar si estamos editando o agregando una playera
        if 'editar' in request.POST:
            # Editar playera
            playera = get_object_or_404(Playera, pk=request.POST['editar'])
            form = PlayeraForm(request.POST, request.FILES, instance=playera)
        elif 'eliminar' in request.POST:
            # Eliminar playera
            playera = get_object_or_404(Playera, pk=request.POST['eliminar'])
            playera.delete()
            return redirect('productos:gestion_playeras')
        else:
            # Crear una nueva playera
            form = PlayeraForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('productos:gestion_playeras')
    else:
        # Mostrar el formulario vacío para crear
        form = PlayeraForm()

    # Obtener todas las playeras para mostrarlas en la tabla
    playeras = Playera.objects.all()

    return render(request, 'productos/gestion_playeras.html', {
        'form': form,
        'playeras': playeras,
    })

# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pedido

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'productos/lista_pedidos.html', {'pedidos': pedidos})

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pedido

# Vista para que los administradores vean y actualicen los pedidos
@login_required(login_url='usuarios:login')
def lista_pedidos_admin(request):
    pedidos = Pedido.objects.all()  # Obtenemos todos los pedidos
    return render(request, 'productos/lista_pedidos_admin.html', {'pedidos': pedidos})

# Vista para actualizar el estado del pedido
@login_required(login_url='usuarios:login')
def actualizar_estado_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)

    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        pedido.estado = nuevo_estado
        pedido.save()

    return render(request, 'productos/lista_pedidos_admin.html', {'pedidos': Pedido.objects.all()})

from django.shortcuts import render, get_object_or_404
from .models import Pedido

def detalles_pedido(request, pedido_id):
    # Obtener el pedido usando el ID
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    # Obtener la personalización asociada al pedido
    personalizacion = pedido.personalizacion
    
    # Pasar los datos a la plantilla
    return render(request, 'productos/detalles_pedido.html', {'pedido': pedido, 'personalizacion': personalizacion})












