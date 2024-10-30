from django.shortcuts import render, redirect
from web.forms import ContactFormForm
from .models import pets
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


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


def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/exito")
    else:
        form = ContactFormForm()
    return render(request, "contacto.html", {"form": form})


def exito(request):
    return render(request, "exito.html")


@login_required
def bienvenido(request):
    return render(request, "welcome.html")
