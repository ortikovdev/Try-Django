from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image', 'author', 'description', 'tags']
        exclude = ['author']

    def __int__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_title",
            "placeholder": "Title",
        })
        self.fields['image'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_title",
        })
        self.fields['description'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_description",
            "rows": 4,
        })
        self.fields['tags'].widget.attrs.update({
            "class": "form-control",
            "id": "recipe_tags",
        })
