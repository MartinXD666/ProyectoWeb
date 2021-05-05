from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "ProyectoWebAPP/home.html")

def servicios(request):

    return render(request, "ProyectoWebAPP/servicios.html")

def tienda(request):

    return render(request, "ProyectoWebAPP/tienda.html")

def blog(request):

    return render(request, "ProyectoWebAPP/blog.html")

def contacto(request):

    return render(request, "ProyectoWebAPP/contacto.html")
