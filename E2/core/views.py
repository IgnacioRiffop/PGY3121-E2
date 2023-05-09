from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

## VIEWS - URLS - HTML

def index(request):
    productosAll = Producto.objects.all() # SELECT * FROM producto
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    
    try:
        paginator = Paginator(productosAll, 3)
        productosAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'listado': productosAll,
        'paginator': paginator
    }
    return render(request, 'core/index.html', data)

def indexSesion(request):
    return render(request, ('core/indexSesion.html'))

# CRUD PRODUCTO
def addProducto(request):
    data = {
        'form' : ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # OBTIENE LA DATA DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() 
            #data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/addProducto.html', data)

def updateProducto(request, id):
    producto = Producto.objects.get(id=id) #OBTIENE UN PRODUCTO POR EL ID
    data = {
        'form' : ProductoForm(instance=producto) # CARGAMOS EL PRODUCTO EN EL FORM
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=producto, files=request.FILES) # OBTIENE LA DATA DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() 
            #data['msj'] = "Producto actualizado correctamente"
            messages.success(request, "Producto almacenado correctamente")
            data['form'] = formulario #CARGA LA NUEVA INFO EN EL FORM
            
    return render(request, 'core/updateProducto.html', data)

def deleteProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect(to='index')
# FIN CRUD PRODUCTO

def carrito(request):
    return render(request, ('core/carrito.html'))

def compra(request):
    return render(request, ('core/compra.html'))

def cuenta(request):
    return render(request, ('core/cuenta.html'))

def tienda(request):
    productosAll = Producto.objects.all() # SELECT * FROM producto
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    
    try:
        paginator = Paginator(productosAll, 9)
        productosAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'listado': productosAll,
        'paginator': paginator
    }
    return render(request, 'core/tienda.html', data)

def tiendaSesion(request):
    return render(request, ('core/tiendaSesion.html'))

def login(request):
    return render(request, ('core/login.html'))

def registro(request):
    return render(request, ('core/registro.html'))

def producto(request):
    return render(request, ('core/producto.html'))

def productoSesion(request):
    return render(request, ('core/productoSesion.html'))

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

