from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fieldsets = [
        (
            "Category name",
            {
                "fields": ["name"]
            }
        ),
        (
            "Write a summary about this category",
            {
                "fields": ["desc"]
            }
        )
    ]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
