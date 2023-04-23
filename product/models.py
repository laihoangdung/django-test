from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    vintage = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True, auto_now_add=False)