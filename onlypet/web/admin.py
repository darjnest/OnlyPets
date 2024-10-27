from django.contrib import admin
from .models import pets, ContactForm

# Register your models here.
admin.site.register(pets)

admin.site.register(ContactForm)
