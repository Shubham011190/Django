from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import Topic,WebPage,AccessRecord


# Create your views here.
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'accessrecord': webpages_list}
    return render(request,'firstapp/index.html',context=date_dict)
