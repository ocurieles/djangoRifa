from django.contrib import admin
from miApp.models import Rifas,Premios, Venta

class RifasAdmin (admin.ModelAdmin):
    list_display = ['nombre','fecha_inicio','fecha_termino','descripcion','numeros_disponibles','numeros_vendidos','estado','imagen']

class PremiosAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","imagen","rifas"]

class VentaAdmin(admin.ModelAdmin):
    list_display= ["nombre","email","telefono","numero_compra","codigo"]

class participanteAdmin(admin.ModelAdmin):
    list_display = ["id","nombre","email","winner"]

admin.site.register(Rifas,RifasAdmin)
admin.site.register(Premios,PremiosAdmin)
admin.site.register(Venta,VentaAdmin)


