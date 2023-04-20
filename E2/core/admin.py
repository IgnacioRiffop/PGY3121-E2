from django.contrib import admin
from .models import *

# Register your models here.

# DEJA EN MODO TABLA LA VISUALIZACION EN EL ADMIN
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','tipo']
    search_fields = ['nombre']
    list_per_page = 10

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)