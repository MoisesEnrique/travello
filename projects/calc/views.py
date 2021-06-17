from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

# Creamos la funcion home, para que funcione con la creada en urls.py.
def home(request):   #recibira la solicitud del cliente
    return HttpResponse("Hello World")