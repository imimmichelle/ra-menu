from typing import Any
from django import forms
from desire_app.models import Category

class ChooseCategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select)



