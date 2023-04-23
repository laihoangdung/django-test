from django.contrib import admin
from .models import Company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    ordering = ["id"]

    class Meta:
        model = Company
        fields = ["name"]


admin.site.register(Company, CompanyAdmin)
