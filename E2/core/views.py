from django.shortcuts import render

# Create your views here.

## VIEWS - URLS - HTML

def index(request):
    return render(request, ('core/index.html'))

def carrito(request):
    return render(request, ('core/carrito.html'))