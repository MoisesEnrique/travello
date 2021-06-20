from django.shortcuts import render

#importamos de models la clase Destination
from .models import Destination

# Create your views here.

# Creamos la funcion index, para que funcione con la creada en travello/urls.py.
def index(request):   #recibira la solicitud del cliente
    
    dest1 = Destination()
    dest1.name = 'Trujillo'
    dest1.desc = "La ciudad de la Eterna Primavera"
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Arequipa'
    dest2.desc = "La ciudad Blanca"
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest1.offer = True

    dest3 = Destination()
    dest3.name = 'Puno'
    dest3.desc = "Capital Folklorica del Perú"
    dest3.img = 'destination_3.jpg'
    dest3.price = 600
    dest1.offer = False

    #creamos una lista de destinos
    dests = [dest1, dest2, dest3]

    return render(request, 'index.html', {'dests': dests}) #le estamos pasando al index.html la lista de destinos