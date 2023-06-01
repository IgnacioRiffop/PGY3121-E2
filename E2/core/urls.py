from django.urls import path, include
from.views import *
from rest_framework import routers

# CREAMOS LAS RUTAS DEL API
router = routers.DefaultRouter()
router.register('productos', ProductoViewset)
router.register('tipoproductos', TipoProductoViewset)

## SE VAN A CREAR TODAS LAS URLS
urlpatterns = [
    #API
    path('api/', include(router.urls)),
    #RUTAS
    path('', index, name="index"),
    path('indexApi/', indexApi, name="indexApi"),
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
    path('miSuscripcion/', miSuscripcion, name="miSuscripcion"),
    path('addSuscripcion/<id>/', addSuscripcion, name="addSuscripcion"),
    path('deleteSuscripcion/<id>/', deleteSuscripcion, name="deleteSuscripcion"),
    path('updateSuscripcion/<id>/', updateSuscripcion, name="updateSuscripcion"),
    path('suscripcionAdmin/', suscripcionAdmin, name="suscripcionAdmin"),
    path('voucher/', voucher, name="voucher"),
    path('recuperarPass/', recuperarPass, name="recuperarPass"),
    path('base/', base, name="base"),
    path('administracion/', administracion, name="administracion"),
    path('adminProductos/', adminProductos, name="adminProductos"),
]
