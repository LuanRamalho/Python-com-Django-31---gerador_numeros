from django.contrib import admin
from .models import Numero

@admin.register(Numero)
class NumeroAdmin(admin.ModelAdmin):
    list_display = ('numero_id', 'valor', 'criado_em')  # Alterado 'id' para 'numero_id'
    ordering = ('-criado_em',)  
    search_fields = ('valor',)
