from django.http.response import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse, request

# Create your views here.

# Creamos la funcion home, para que funcione con la creada en urls.py.
def home(request):   #recibira la solicitud del cliente
    return render(request, 'home.html', {'name':'Ricardo'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])

    res = val1 + val2

    return render(request, "result.html", {'result':res})