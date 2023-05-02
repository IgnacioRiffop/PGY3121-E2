# FORMULARIO PARA AGREGAR Y ACTUALIZAR 
from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm (ModelForm):
    class Meta:
        model = Producto
        #fields = ['nombre','precio','stock','descripcion','tipo']
        fields = '__all__'