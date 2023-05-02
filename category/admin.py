from django.contrib import admin, messages
from category.models import Category
from django import forms


def show_error(func):
    def wrapper(*args, **kwargs):
        print("args: ", args)
        try:
            return func(*args, **kwargs)
        except Exception as e:
            messages.set_level(args[1], messages.ERROR)
            messages.error(args[1], e)

    return wrapper


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

    @show_error
    def delete_model(self, request, obj):
        return super(CategoryAdmin, self).delete_model(request, obj)

    @show_error
    def delete_queryset(self, request, queryset):
        return super(CategoryAdmin, self).delete_queryset(request, queryset)

    # def delete_model(self, request, obj):
    #     try:
    #         super(CategoryAdmin, self).delete_model(request, obj)
    #     except Exception as e:
    #         print("test error")
    #         print(e)
    #         messages.set_level(request, messages.ERROR)
    #         messages.error(request, e)

    # def delete_queryset(self, request, queryset):
    #     try:
    #         super(CategoryAdmin, self).delete_queryset(request, queryset)
    #     except Exception as e:
    #         print("test error")
    #         print(e)
    #         messages.set_level(request, messages.ERROR)
    #         messages.error(request, e)


# Register your models here.
admin.site.register(Category, CategoryAdmin)
