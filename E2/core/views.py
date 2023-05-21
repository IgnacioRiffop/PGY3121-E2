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
    return redirect(to='adminProductos')
# FIN CRUD PRODUCTO


def carrito(request):
    cliente = Cliente.objects.filter(usuario=request.user.username)[:1]
    CarritoCliente = Carrito.objects.filter(cliente=cliente)

    data = {
        'listado': CarritoCliente
    }

    return render(request, 'core/carrito.html', data)

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

def producto(request, id):
    producto = Producto.objects.get(id=id)
    try:
        cliente = Cliente.objects.get(usuario=request.user.username)
    except Cliente.DoesNotExist:
        cliente = None
    data = {
        'producto': producto,
        'usuario': request.user.username,
        'form' : CantidadForm(initial={'cantidad': 1})
    }

    if request.method == 'POST':
        formulario = CantidadForm(request.POST, files=request.FILES) # OBTIENE LA DATA DEL FORMULARIO
        if formulario.is_valid():
            #Carrito.objects.all().delete()
            carrito = Carrito.objects.create(cliente=cliente,producto=producto,cantidad=formulario.data["cantidad"])
            #carrito.producto.add(producto)

            
    return render(request, ('core/producto.html'), data)

def productoSesion(request):
    return render(request, ('core/productoSesion.html'))

def suscripcion(request):
    basica = TipoSuscripcion.objects.get(id=1)
    intermedia = TipoSuscripcion.objects.get(id=2)
    alta = TipoSuscripcion.objects.get(id=3)
    
    cliente = Cliente.objects.filter(usuario=request.user.username)[:1]
    try:
        suscripcionCliente = Suscripcion.objects.get(cliente=cliente)
    except Suscripcion.DoesNotExist:
        suscripcionCliente = None

    data = {
        'basica': basica,
        'intermedia': intermedia,
        'alta' : alta,
        'suscripcionCliente' : suscripcionCliente

    }
    return render(request, 'core/suscripcion.html', data)

def suscripcionAdmin(request):
    basica = TipoSuscripcion.objects.get(id=1)
    intermedia = TipoSuscripcion.objects.get(id=2)
    alta = TipoSuscripcion.objects.get(id=3)
    
    cliente = Cliente.objects.filter(usuario=request.user.username)[:1]
    try:
        suscripcionCliente = Suscripcion.objects.get(cliente=cliente)
    except Suscripcion.DoesNotExist:
        suscripcionCliente = None

    data = {
        'basica': basica,
        'intermedia': intermedia,
        'alta' : alta,
        'suscripcionCliente' : suscripcionCliente

    }
    return render(request, 'core/suscripcionAdmin.html', data)

def miSuscripcion(request):
    basica = TipoSuscripcion.objects.get(id=1)
    intermedia = TipoSuscripcion.objects.get(id=2)
    alta = TipoSuscripcion.objects.get(id=3)
    
    cliente = Cliente.objects.filter(usuario=request.user.username)[:1]
    try:
        suscripcionCliente = Suscripcion.objects.get(cliente=cliente)
    except Suscripcion.DoesNotExist:
        suscripcionCliente = None

    data = {
        'basica': basica,
        'intermedia': intermedia,
        'alta' : alta,
        'suscripcionCliente' : suscripcionCliente

    }
    return render(request, 'core/miSuscripcion.html', data)

# CRUD Suscripcion
def addSuscripcion(request, id):
    cliente = Cliente.objects.get(usuario=request.user.username)
    tipoSuscripcion = TipoSuscripcion.objects.get(id=id)
    suscripcion = Suscripcion.objects.create(cliente=cliente, suscripcion=tipoSuscripcion)
    return redirect(to='suscripcion')

def deleteSuscripcion(request, id):
    cliente = Cliente.objects.filter(usuario=request.user.username)[:1]
    suscripcionCliente = Suscripcion.objects.get(cliente=cliente)
    suscripcionCliente.delete()
    return redirect(to='suscripcion')

def updateSuscripcion(request, id):
    cliente = Cliente.objects.filter(usuario=request.user.username)[:1]
    tipoSuscripcion = TipoSuscripcion.objects.get(id=id)
    suscripcionCliente = Suscripcion.objects.get(cliente=cliente)
    suscripcionCliente.suscripcion = tipoSuscripcion
    suscripcionCliente.save()
    return redirect(to='suscripcion')
# FIN CRUD Suscripcion

def voucher(request):
    return render(request, ('core/voucher.html'))

def recuperarPass(request):
    return render(request, ('core/recuperarPass.html'))

def base(request):
    return render(request, ('core/base.html'))

def administracion(request):
    return render(request, ('core/administracion.html'))

def adminProductos(request):
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
    return render(request, 'core/adminProductos.html', data)

# CRUD CARRITO
def deleteCarrito(request, id):
    itemCarrito = Carrito.objects.get(id=id)
    usuario = itemCarrito.cliente
    itemCarrito.delete()
    return redirect(to='carrito')
# FIN CRUD CARRITO

