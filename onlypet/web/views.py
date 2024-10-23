from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def welcome(request):
    context = {"nombre_usuario": "Carlos Silva"}  # O None si no hay usuario
    return render(request, "welcome.html", context)
