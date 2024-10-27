from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("acerca/", views.about, name="about"),
    path("bienvenido/", views.welcome, name="welcome"),
    path("ventas/", views.ventas, name="ventas"),
    path("contacto/", views.contacto, name="contacto"),
    path("exito/", views.exito, name="exito"),
]
