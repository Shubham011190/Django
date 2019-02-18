from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    my_dict={'insert':'Welcome!'}
    return render(request,'index.html',context=my_dict)
