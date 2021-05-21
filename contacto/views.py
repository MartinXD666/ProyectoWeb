from .forms import FormularioContacto
from django.shortcuts import render

# Create your views here.

def contacto(request):

    formulario_contacto=FormularioContacto()
    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
