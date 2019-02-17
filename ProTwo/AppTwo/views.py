from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Project 2")

# Create your views here.
