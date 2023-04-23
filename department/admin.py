from django.contrib import admin
from .models import Department


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "company", "name"]
    ordering = ["id"]

    class Meta:
        model = Department
        fields = ["company", "name"]


admin.site.register(Department, DepartmentAdmin)
