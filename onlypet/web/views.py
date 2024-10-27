from django.shortcuts import render
from .models import pets


def index(request):
    mascotas_publicos = pets.objects.filter(is_private=False)
    return render(request, "index.html", {"pets": mascotas_publicos})


def about(request):
    return render(request, "about.html")


def welcome(request):
    mascotas_privados = pets.objects.filter(is_private=True)
    return render(request, "welcome.html", {"pets": mascotas_privados})


def ventas(request):
    return render(request, "ventas.html")
