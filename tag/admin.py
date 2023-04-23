from django.contrib import admin
from tag.models import Tag
from django import forms


# Register your models here.
class TagForm(forms.ModelForm):
    def clean(self):
        name = self.cleaned_data["name"]
        isTagExisted = Tag.objects.filter(name=name).exists()
        if isTagExisted:
            raise forms.ValidationError({"name": "Tag name existed"})


class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    ordering = ["id"]
    form = TagForm


admin.site.register(Tag, TagAdmin)