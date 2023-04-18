from django.urls import path
from.views import index
from.views import carrito

## SE VAN A CREAR TODAS LAS URLS
urlpatterns = [
    path('', index, name="index"),
    path('carrito/', carrito, name="carrito"),
]
