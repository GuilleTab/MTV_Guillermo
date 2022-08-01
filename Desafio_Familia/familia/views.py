from django.shortcuts import render
from django.template import Template, Context

from django.http import HttpResponse
from familia.models import mi_familia

def info_familia(request):
    return HttpResponse("<h1>DATOS DE MIS FAMILIARES</h1>")


def inicio(request):
    mi_template = open(r"C:\Users\guill\OneDrive\Escritorio\Python\MVT_Guillermo\Desafio_Familia\mis_familiares\templates\index.html", "r")

    plantilla = Template(mi_template.read())
    mi_template.close()

    contexto = Context()

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


def lista_familia(request):
    familiares = mi_familia.objects.all()

    return render(request, "index.html", {"familiares":familiares})
