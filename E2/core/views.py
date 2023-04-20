from django.shortcuts import render

# Create your views here.

## VIEWS - URLS - HTML

def index(request):
    return render(request, ('core/index.html'))

def carrito(request):
    return render(request, ('core/carrito.html'))

def compra(request):
    return render(request, ('core/compra.html'))

def cuenta(request):
    return render(request, ('core/cuenta.html'))

def tienda(request):
    return render(request, ('core/tienda.html'))

def login(request):
    return render(request, ('core/login.html'))

def registro(request):
    return render(request, ('core/registro.html'))

def producto(request):
    return render(request, ('core/producto.html'))

def suscripcion(request):
    return render(request, ('core/suscripcion.html'))

def suscripcionAdmin(request):
    return render(request, ('core/suscripcionAdmin.html'))

def voucher(request):
    return render(request, ('core/voucher.html'))

def recuperarPass(request):
    return render(request, ('core/recuperarPass.html'))

def base(request):
    return render(request, ('core/base.html'))

