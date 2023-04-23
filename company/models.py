from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
