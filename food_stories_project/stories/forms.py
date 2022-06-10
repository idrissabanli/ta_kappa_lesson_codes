from django import forms
from stories.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'short_description',
            'content',
            'image',
            'category',
            # 'author',
            'tags',
        )