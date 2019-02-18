from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    my_dict={'insert':'Hola! I am from views.py'}
    return render(request,'firstapp/index.html',context=my_dict)
