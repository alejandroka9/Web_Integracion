from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def cargarInicio(request):
    productos = Producto.objects.all()
    producto_notebook = Producto.objects.filter(categoria_id=1)
    producto_celular = Producto.objects.filter(categoria_id=2)
    return render(request,"inicio.html",{"prod" : productos, "prod_note":producto_notebook, "prod_cel":producto_celular})


def cargarAgregarProducto(request):
    categorias = Categoria.objects.all()
    return render(request, "agregarProducto.html",{"cate":categorias})

def registro(request):

    return render(request, "registro.html")

def iniciar(request):
    
    return render(request, "iniciar.html")

def agregarProducto(request):
    #print("AGREGANDO PRODUCTOS A LA BBDD",request.POST)
    v_sku = request.POST['txtSku']
    v_precio = request.POST['txtPrecio']
    v_nombre = request.POST['txtNombre']
    v_imagen = request.POST['txtImagen']
    v_descripcion = request.POST['txtDescripcion']
    v_stock = request.POST['txtStock']

    v_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    Producto.objects.create(sku = v_sku, precio = v_precio, nombre = v_nombre,imagen = v_imagen,descripcion = v_descripcion,stock = v_stock, categoria_id = v_categoria)


    return redirect('/agregarProducto')

