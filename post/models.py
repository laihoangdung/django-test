from django.db import models
from category.models import Category


# Create your models here.
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    author_name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    # def save(self, *args, **kwargs):
    #     if not self.pub_date:
    #         self.pub_date = None
    #         super(Post, self).save(*args, **kwargs)
