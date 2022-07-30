from django.shortcuts import render
from django.template import Template, Context

from django.http import HttpResponse
from familia.models import mi_familia

def info_familia(request):
    return HttpResponse("DATOS DE MIS FAMILIARES")


def inicio(request):
    mi_template = open(r"C:\Users\guill\OneDrive\Escritorio\Python\MVT_Guillermo\Desafio_Familia\mis_familiares\templates\index.html", "r")

    plantilla = Template(mi_template.read())
    mi_template.close()

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def lista_familia(request):
    familia = mi_familia.objects.all()
    datos_familia = []

    for persona in familia:
        datos_familia.append(mi_familia.nombre)

    return HttpResponse(datos_familia)
