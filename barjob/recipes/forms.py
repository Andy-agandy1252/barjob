from django import forms
from .models import Recipe
from django.core.exceptions import ValidationError

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name', 'code', 'category',
            'image1', 'image2', 'image3', 'image4', 'image5',
            'image6', 'image7', 'image8', 'image9', 'image10'
        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        code = cleaned_data.get('code')

        # Ensure that the name is unique (but not for the current recipe)
        if name and Recipe.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            raise ValidationError({'name': 'This recipe name is already taken. Please choose a different one.'})

        # Ensure that the code is unique (but not for the current recipe)
        if code and Recipe.objects.filter(code=code).exclude(pk=self.instance.pk).exists():
            raise ValidationError({'code': 'This recipe code is already taken. Please choose a different one.'})

        return cleaned_data

class RecipeSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label="Search by Name or Code")