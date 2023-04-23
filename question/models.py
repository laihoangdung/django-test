from django.db import models
from tag.models import Tag


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class QuestionTag(models.Model):
    question = models.ForeignKey(Question, on_delete=models.Case)
    tag = models.ForeignKey(Tag, on_delete=models.Case)
