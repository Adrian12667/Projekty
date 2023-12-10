from django.contrib import admin
from .models import Kategoria, Produkt


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'etykieta']
    prepopulated_fields = {'etykieta': ('nazwa',)}


@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'etykieta', 'cena',
                    'dostepne', 'utworzono', 'aktualizacja']
    list_filter = ['dostepne', 'utworzono', 'aktualizacja']
    list_editable = ['cena', 'dostepne']
    prepopulated_fields = {'etykieta': ('nazwa',)}




