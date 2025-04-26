from django.contrib import admin
from .models import Alimento, Roupa, HigienePessoal

@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'quantidade', 'data_validade')
    search_fields = ('nome',)
    list_filter = ('data_validade',)

@admin.register(Roupa)
class RoupaAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'tamanho', 'quantidade')
    search_fields = ('tipo', 'tamanho')
    list_filter = ('tamanho',)

@admin.register(HigienePessoal)
class HigienePessoalAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'quantidade')
    search_fields = ('tipo',)
