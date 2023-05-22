from django.contrib import admin
from .models import *

# Register your models here.

# DEJA EN MODO TABLA LA VISUALIZACION EN EL ADMIN
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','descripcion','tipo','fecha','imagen']
    search_fields = ['nombre']
    list_per_page = 10
    list_filter = ['tipo']
    list_editable = ['precio','stock','descripcion','tipo','fecha','imagen']

class CarritoAdmin(admin.ModelAdmin):
    list_display = ['cliente','producto','cantidad']
    #search_fields = ['cliente']
    list_per_page = 10
    list_filter = ['cliente']
    list_editable = ['producto','cantidad']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['usuario','nombre','apellido','email','password']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']
    list_editable = ['nombre','apellido','email','password']

class SuscripcionAdmin(admin.ModelAdmin):
    list_display = ['cliente','suscripcion']
    #search_fields = ['cliente']
    list_per_page = 10
    list_filter = ['cliente']
    list_editable = ['suscripcion']

class TProductoAdmin(admin.ModelAdmin):
    list_display = ['descripcion']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']

class TSuscripcionAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio']
    #search_fields = ['cliente']
    list_per_page = 10
    #list_filter = ['cliente']
    list_editable = ['precio']

class CompraAdmin(admin.ModelAdmin):
    list_display = ['cliente','direccion','contacto']
    #search_fields = ['cliente']
    list_per_page = 10
    list_filter = ['cliente']
    list_editable = ['direccion','contacto']

admin.site.register(TipoProducto,TProductoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Carrito, CarritoAdmin)
admin.site.register(Compras,CompraAdmin)
admin.site.register(TipoSuscripcion,TSuscripcionAdmin)
admin.site.register(Suscripcion,SuscripcionAdmin)