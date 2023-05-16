from django.contrib import admin
from .models import Contacto

class AdminContacto(admin.ModelAdmin):
    list_display = ["__str__","nombre","apellido","email"]
    class Meta(object):
        model = Contacto
admin.site.register(Contacto, AdminContacto)
# Register your models here.
