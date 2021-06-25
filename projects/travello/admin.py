from django.contrib import admin

#importamos del modelo la clase Destination
from .models import Destination


# Register your models here.
admin.site.register(Destination)