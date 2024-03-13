from typing import Any
from django import forms
from desire_app.models import Desire, Category

class DesireForm(forms.ModelForm):
    class Meta():
        model = Desire
        fields = '__all__'
    desire_name = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select, initial='')

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'
    category_name = forms.CharField()

class DesiresForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'
    desire_list = forms.CharField(widget=forms.Textarea)
    