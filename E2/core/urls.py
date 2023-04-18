from django.urls import path
from.views import *

## SE VAN A CREAR TODAS LAS URLS
urlpatterns = [
    path('', index, name="index"),
    path('carrito/', carrito, name="carrito"),
    path('compra/', compra, name="compra"),
    path('cuenta/', cuenta, name="cuenta"),
    path('tienda/', tienda, name="tienda"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('producto/', producto, name="producto"),
    path('suscripcion/', suscripcion, name="suscripcion"),
    path('suscripcionAdmin/', suscripcionAdmin, name="suscripcionAdmin"),
    path('voucher/', voucher, name="voucher"),
    path('recuperarPass/', recuperarPass, name="recuperarPass"),
]
