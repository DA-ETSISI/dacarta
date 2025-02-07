from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import messages

from .models import carta

admin.site.site_header = 'DA-nos tu opinión'
admin.site.index_title = 'DA-nos tu opinión'
admin.site.site_title = 'DA-nos tu opinión'


class CartaAdmin(admin.ModelAdmin):
    list_display = ("asunto", "fecha", "etiqueta")
    search_fields = ("asunto", "etiqueta")
    list_filter = ("etiqueta",)

    def MarcarTramitado(modeladmin, request, queryset):
        queryset.update(etiqueta="Tra")
        messages.success(request, "Se han marcado las cartas")

    admin.site.add_action(MarcarTramitado, "Marcar como tramitado")


admin.site.register(carta, CartaAdmin)