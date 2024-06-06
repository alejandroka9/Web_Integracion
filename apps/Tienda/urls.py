from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.cargarInicio),
    path('agregarProducto', views.cargarAgregarProducto),
    path('agregarProductoForm', views.agregarProducto),
    path('registro', views.registro),  
    path('iniciar', views.iniciar),
    path('inicio', views.cargarInicio),
]
