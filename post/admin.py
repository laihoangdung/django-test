from django.contrib import admin
from post.models import Post
from django import forms
from category.models import Category


# class PostForm(forms.ModelForm):
#     pub_date = forms.DateTimeField()
#     author_name = forms.CharField(allow_null=True, default=None)
#
#     class Meta:
#         model = Post
#         fields = ["category", "name", "content", "pub_date", "author_name"]
#
    # def clean(self):
    #     print("clean: ", self.cleaned_data)
    #     if "pub_date" not in self.cleaned_data:
    #         self.cleaned_data["pub_date"] = None
    #     if "author_name" not in self.cleaned_data:
    #         self.cleaned_data["author_name"] = None


# class PostForm(forms.BaseModelForm):
#     # category = forms.Fe(Category)
#     name = forms.CharField(required=True, max_length=255)
#     content = forms.Textarea()
#     pub_date = forms.DateTimeField()
#     author_name = forms.CharField(required=True)


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    # fields = ["category", "name", "content", "pub_date", "author_name"]
    # fieldsets = ()
    # form = PostForm

    def save_model(self, request, obj, form, change):
        print("go post save custom")
        # print("pub_date: ", request.pub_date)
        super().save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Post, PostAdmin)
