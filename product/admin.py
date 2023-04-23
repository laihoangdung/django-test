from django.contrib import admin
from product.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    search_fields = ["title"]
    list_filter = ["vintage"]


admin.site.register(Product, ProductAdmin)
