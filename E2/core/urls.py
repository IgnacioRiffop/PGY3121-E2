from django.urls import path
from.views import *

## SE VAN A CREAR TODAS LAS URLS
urlpatterns = [
    path('', index, name="index"),
    path('indexSesion', indexSesion, name="indexSesion"),
    path('addProducto', addProducto, name="addProducto"),
    path('updateProducto/<id>/', updateProducto, name="updateProducto"),
    path('deleteProducto/<id>/', deleteProducto, name="deleteProducto"),
    path('deleteCarrito/<id>/', deleteCarrito, name="deleteCarrito"),
    path('tiendaSesion', tiendaSesion, name="tiendaSesion"),
    path('productoSesion', productoSesion, name="productoSesion"),
    path('carrito/', carrito, name="carrito"),
    path('compra/', compra, name="compra"),
    path('cuenta/', cuenta, name="cuenta"),
    path('tienda/', tienda, name="tienda"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('producto/<id>', producto, name="producto"),
    path('suscripcion/', suscripcion, name="suscripcion"),
    path('suscripcionAdmin/', suscripcionAdmin, name="suscripcionAdmin"),
    path('voucher/', voucher, name="voucher"),
    path('recuperarPass/', recuperarPass, name="recuperarPass"),
    path('base/', base, name="base"),
]
