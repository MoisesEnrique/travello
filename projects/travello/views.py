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
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Puno'
    dest3.desc = "Capital Folklorica del Perú"
    dest3.img = 'destination_3.jpg'
    dest3.price = 600
    dest3.offer = False

    dest4 = Destination()
    dest4.name = 'Cusco'
    dest4.desc = "Capital Arqueoilogica de América"
    dest4.img = 'destination_4.jpg'
    dest4.price = 600
    dest4.offer = True

    dest5 = Destination()
    dest5.name = 'Nazca'
    dest5.desc = "Conoce las lineas de Nazca"
    dest5.img = 'destination_5.jpg'
    dest5.price = 600
    dest5.offer = False

    dest6 = Destination()
    dest6.name = 'Iquitos'
    dest6.desc = "De la selva su gente"
    dest6.img = 'destination_6.jpg'
    dest6.price = 600
    dest6.offer = False

    dest7 = Destination()
    dest7.name = 'Piura'
    dest7.desc = "La Ciudad del Norte"
    dest7.img = 'destination_13.jpg'
    dest7.price = 600
    dest7.offer = False

    dest8 = Destination()
    dest8.name = 'Tacna'
    dest8.desc = "La Ciudad Heroica"
    dest8.img = 'destination_14.jpg'
    dest8.price = 600
    dest8.offer = True

    dest9 = Destination()
    dest9.name = 'Huancayo'
    dest9.desc = "La Incontrastable"
    dest9.img = 'destination_15.jpg'
    dest9.price = 600
    dest9.offer = False

    dest10 = Destination()
    dest10.name = 'Lima'
    dest10.desc = "Capital del Perú"
    dest10.img = 'destination_10.jpg'
    dest10.price = 600
    dest10.offer = False

    dest11 = Destination()
    dest11.name = 'Apurimac'
    dest11.desc = "La ciudad de los Chankas"
    dest11.img = 'destination_11.jpg'
    dest11.price = 600
    dest11.offer = True

    dest12 = Destination()
    dest12.name = 'Cajamarca'
    dest12.desc = "El Carnaval del Norte"
    dest12.img = 'destination_12.jpg'
    dest12.price = 600
    dest12.offer = False

    #creamos una lista de destinos
    dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8, dest9, dest10, dest11, dest12]

    return render(request, 'index.html', {'dests': dests}) #le estamos pasando al index.html la lista de destinos