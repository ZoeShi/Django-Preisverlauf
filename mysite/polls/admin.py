from django.contrib import admin

# Register your models here.



from .models import Preis
from .models import Product

class PreisAdmin(admin.ModelAdmin):

    fields = ["Product", "Alter_Preis", "Neuer_Preis", "datumzeit"]

    list_display = ('Product', 'Alter_Preis', 'Neuer_Preis','datumzeit')
    search_fields = ['Product__Product']
    list_filter = ['datumzeit']
admin.site.register(Preis, PreisAdmin)


class ProductAdmin(admin.ModelAdmin):

    fields = ["Product", "GuenstigsterPreis", "Kategorie"]

    list_display = ('Product', 'GuenstigsterPreis')
    search_fields = ['Product', 'GuenstigsterPreis']
admin.site.register(Product, ProductAdmin)
