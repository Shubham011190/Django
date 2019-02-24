from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'ProTwo/index.html')

def users(request):
    users_list=User.objects.order_by('firstName')
    users_dict={'userdict':users_list}
    return render(request,'ProTwo/users.html',context=users_dict)
    
