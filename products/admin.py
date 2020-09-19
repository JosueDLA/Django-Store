from django.contrib import admin
from .models import ProductType, Product

# Register your models here.


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('name', 'stock', 'entry_date')


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
