from django.db import models
from company.models import Company


# Create your models here.
class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{} - {}".format(self.company.name, self.name)
