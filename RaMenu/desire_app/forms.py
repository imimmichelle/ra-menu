from typing import Any
from django import forms
from desire_app.models import Desire, Category

class DesireForm(forms.ModelForm):
    class Meta():
        model = Desire
        fields = '__all__'
    desire_name = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select)

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'