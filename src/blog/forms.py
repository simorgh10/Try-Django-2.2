from django import forms

from .models import BlogPost


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'slug', 'content']

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     qs = BlogPost.objects.filter(title__iexact=title)
    #     if qs.exists():
    #         raise forms.ValidationError("This title has already been used. Please try again.")
    #     return title
