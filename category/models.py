from django.db import models


# Create your models here.
class Category(models.Model):
    DRAFT = "Draft"
    LIVE = "Live"

    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (LIVE, "Live"),
    ]

    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name
