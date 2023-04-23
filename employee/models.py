from django.db import models
from department.models import Department


# Create your models here.
class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    dob = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True, auto_now_add=False)
