from django import forms
from django.core.exceptions import ValidationError
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Here title is written...'}),
            'content': forms.Textarea(attrs={'placeholder': 'Here content is written...'}),
        }

    def clean_title(self): # clean_{filed_name}
        if self.cleaned_data['title'].replace(" ", "").isalnum():
            return self.cleaned_data['title']
        raise ValidationError('title must be alpha numeric')