from django.contrib import admin
from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "status"]
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
        ),
        (
            "Status",
            {
                "fields": ["status"]
            }
        )
    ]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
