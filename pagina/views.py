import json
import re
from textwrap import indent
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template  import loader
from .models import Usuario

# Create your views here.
def index(request):
    return HttpResponse('Hola Mundo desde Django')

def json(request):

    array= {
        'nombre':'Tito',
        'apellido':'Lopez',
        'edad':12
    }
    return JsonResponse(array, json_dumps_params={'indent':4})

def webpage(request):
    template = loader.get_template('webpage.html')
    return HttpResponse(template.render())


def webpage2(request):
    template = loader.get_template('header.html')
    a = 23
    b = 90


    data = {
        'nombre':request.GET.get('nombre','Diana'),
        'a':a,
        'b':b,
        'suma':a+b
    }
    return HttpResponse(template.render(data,request))


def update(request):
    datos_modelo = Usuario.objects.all().values()
    return JsonResponse(list(datos_modelo),safe=False, json_dumps_params={'indent':4})

def nueva(request):
    template = loader.get_template('pagina_modelo.html')
    datos_modelo = Usuario.objects.all().values()
    data = {
        'nombre':request.GET.get('nombre','Diana'),
        'usuarios':Usuario.objects.all().values()
    }
    return HttpResponse(template.render(data,request))