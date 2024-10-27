from email.policy import default
from os import name
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.utils.text import slugify
import uuid


class pets(models.Model):
    pets_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    descripcion = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True, blank=False)
    is_private = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
