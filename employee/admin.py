from django.contrib import admin
from .models import Employee
from company.models import Company
from department.models import Department
from django import forms
from dynamic_forms import DynamicField


# Register your models here.
# class EmployeeForm(DynamicField, forms.ModelForm):
#     company = forms.ModelChoiceField(queryset=Company.objects.all())
#     department = forms.ModelChoiceField(queryset=Department.objects.none())
#
#     def __int__(self, data=None, *args, **kwargs):
#         company = kwargs.pop("company")
#         super().__init__(*args, **kwargs)
#         self.fields["department"].queryset = Department.objects.filter(company=company)
#
#     class Meta:
#         model = Employee
#         fields = ["company", "department", "name"]


class EmployeeForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    # def __int__(self, *args, **kwargs):
    #     print("go to init")
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     company = kwargs["company"]
    #     print("company: ", company)
    #     self.fields["department"].queryset = Department.objects.filter(company=company)

    class Meta:
        model = Employee
        fields = ["company", "department", "name"]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "department", "name"]
    form = EmployeeForm


admin.site.register(Employee, EmployeeAdmin)
