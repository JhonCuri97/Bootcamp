from django.contrib import admin
from apps.sip_telefono.models import (
    marca_telefono,
    modelo_telefono,
    sip_telefono
)
# Register your models here.
admin.site.register(marca_telefono)
admin.site.register(modelo_telefono)
admin.site.register(sip_telefono)

