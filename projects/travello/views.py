from django.shortcuts import render

# Create your views here.

# Creamos la funcion index, para que funcione con la creada en travello/urls.py.
def index(request):   #recibira la solicitud del cliente
    return render(request, 'index.html')