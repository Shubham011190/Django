from django.http import HttpResponse
from django.shortcuts import render
from firstapp.models import Name,Data


# Create your views here.
def index(request):
    urlList=Data.objects.order_by('date')
    date_dict={'dates':'urlList'}
    return render(request,'firstapp/index.html',context=date_dict)
