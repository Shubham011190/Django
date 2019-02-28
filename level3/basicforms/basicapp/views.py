from django.shortcuts import render
from . import forms

def index(request):
    return render(request,'basicapp/index.html')

def formNameView(request):
    form= forms.formName()

    if request.method== 'POST':
        form=forms.formName(request.POST)

        if form.is_valid():
            print("----------\nValidation Successful")
            print('Name: '+form.cleaned_data['name'])
            print('Email : '+form.cleaned_data['email'])
            print('Text : '+form.cleaned_data['text'])
            print('----------\n')

    return render(request,'basicapp/formPage.html',{'form':form})
# Create your views here.
