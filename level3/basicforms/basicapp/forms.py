from django import forms
from django.core import validators

def nameCheck(value):
    if value[0].upper() !='S':
        raise forms.ValidationError('Name should start with S')


class formName(forms.Form):
    name=forms.CharField(validators=[nameCheck])
    email=forms.EmailField()
    verifyMail=forms.EmailField(label='Enter your mail again: ')
    text= forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)


    def clean(self):
        allClean=super().clean()
        email=allClean['email']
        vmail=allClean['verifyMail']
        if email!=vmail:
            raise forms.ValidationError('Make sure Emails match!')
