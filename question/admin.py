from django.contrib import admin
from question.models import Question, QuestionTag
from tag.models import Tag
from django import forms


# Register your models here.
class QuestionForm(forms.ModelForm):
    # def __int__(self, *args, **kwargs):
    #     super(Question, self).__init__(*args, **kwargs)
    #     self.fields['title'].help_text = "New Help Text"
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "class": ""
                                }
                            ))
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Question
        fields = ('title', 'content', 'tags')

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        # tags = instance.tags
        print("tags: ", self.cleaned_data["tags"])
        create_tags = []
        for tag in self.cleaned_data["tags"]:
            tag_existed = QuestionTag.objects.filter(
                question__title=self.cleaned_data["title"],
                tag_id=tag.id,
            ).exists()
            if not tag_existed:
                create_tags.append(QuestionTag(tag=tag))
        # instance = instance.save()
        # print("instance: ", instance)
        if commit:
            print("run in commit")
            print("instance: ", instance)
            instance = instance.save()
            for t in create_tags:
                t.question = instance
                t.save()
        return instance


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    form = QuestionForm
    ordering = ["id"]

    def save_model(self, request, obj, form, change):
        # print("request: ", request)
        # print("object: ", obj)
        # print("form: ", form)
        # print("change: ", change)
        super().save_model(request, obj, form, change)


admin.site.register(Question, QuestionAdmin)
