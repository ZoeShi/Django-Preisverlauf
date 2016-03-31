from django.contrib import admin

# Register your models here.



from .models import Product
from .models import Product_id

class ProductAdmin(admin.ModelAdmin):

    fields = ["Product", "Alter_Preis", "Neuer_Preis", "datumzeit"]

    list_display = ('Product', 'Alter_Preis', 'Neuer_Preis','datumzeit')
    search_fields = ['Product__Product']
    list_filter = ['datumzeit']
admin.site.register(Product, ProductAdmin)


class Product_idAdmin(admin.ModelAdmin):

    fields = ["Product", "GuenstigsterPreis"]

    list_display = ('Product', 'GuenstigsterPreis')
    search_fields = ['Product', 'GuenstigsterPreis']
admin.site.register(Product_id, Product_idAdmin)
