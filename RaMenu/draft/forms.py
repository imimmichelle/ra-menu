from typing import Any
from django import forms
from draft.models import UserDraft, DesireDraft, UserDesireDraft, AnswerDraft

CHOICES = ['unknown', 'NO', 'MAYBE', 'YES']

class UserFormDraft(forms.ModelForm):
    # Form Fields go here with validator parameters
    class Meta():
        model = UserDraft
        fields = '__all__'

class PreferenceFormDraft(forms.ModelForm):
    class Meta():
        model = UserDraft
        fields = ['user_name', 'desires']  
    user_name = forms.ModelChoiceField(queryset=UserDraft.objects.all(), widget=forms.RadioSelect)
    desires = forms.ModelMultipleChoiceField(queryset=DesireDraft.objects.all(), widget=forms.CheckboxSelectMultiple)
    

class DesireFormDraft(forms.ModelForm):
    class Meta():
        model = DesireDraft
        fields = '__all__'

class AnswerFormDraft(forms.ModelForm):
    class Meta():
        model = DesireDraft
        fields = ['desire_name', 'answer']
    answer = forms.ModelChoiceField(queryset=AnswerDraft.objects.all(), widget=forms.CheckboxInput)
    

#class AtomicFormTwoUsers


""" from django.core import validators

def check_for_s(value):
    if value[0].lower() != 's':
        raise forms.ValidationError('name needs to start with S')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_s])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='enter email again')
    text = forms.CharField(widget=forms.Textarea)
    #botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, 
                                #validators=[validators.MaxLengthValidator(0)])


    def clean(self):
        cleaned = super().clean()
        email = cleaned['email']
        verify = cleaned['verify_email']

        if email != verify:
            raise forms.ValidationError('your emails are different')
        
        #return super().clean()
    

 """