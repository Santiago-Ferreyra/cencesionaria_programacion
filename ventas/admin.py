from django.contrib import admin
from .models import Marca, Modelo, Vendedor, Cliente, Venta


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais_origen', 'año_fundacion')
    search_fields = ('nombre', 'pais_origen')
    list_filter = ('pais_origen',)


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'año', 'tipo_combustible', 'precio_lista', 'cantidad_stock')
    list_filter = ('marca', 'tipo_combustible', 'año')
    search_fields = ('nombre', 'marca__nombre')
    readonly_fields = ('cantidad_stock',)


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'legajo', 'fecha_ingreso')
    search_fields = ('nombre', 'apellido', 'legajo')
    list_filter = ('fecha_ingreso',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'telefono', 'email')
    search_fields = ('nombre', 'apellido', 'dni', 'email')
    list_filter = ('apellido',)


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_venta', 'cliente', 'modelo', 'vendedor', 'precio_final', 'metodo_pago')
    list_filter = ('fecha_venta', 'metodo_pago', 'vendedor')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'modelo__nombre', 'vendedor__nombre')
    date_hierarchy = 'fecha_venta'
    readonly_fields = ('id',)

