from django.contrib import admin
from .models import *

# Register your models here.

# DEJA EN MODO TABLA LA VISUALIZACION EN EL ADMIN
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','tipo']
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['tipo']
    list_editable = ['precio','stock','descripcion','tipo']

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(Compras)