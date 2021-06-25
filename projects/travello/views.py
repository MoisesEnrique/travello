from django.shortcuts import render

#importamos de models la clase Destination
from .models import Destination

# Create your views here.

# Creamos la funcion index, para que funcione con la creada en travello/urls.py.
def index(request):   #recibira la solicitud del cliente
    
    dests = Destination.objects.all() #recibe los objetos de la tabla Destinations

    return render(request, 'index.html', {'dests': dests}) #le estamos pasando al index.html la lista de destinos