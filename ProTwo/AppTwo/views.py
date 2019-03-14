#from django.http import HttpResponse
from django.shortcuts import render
from AppTwo.forms import NewUserForm

def index(request):
    return render(request,'index.html')

def users(request):
    form= NewUserForm()
    if request.method=='POST':
        form= NewUserForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)
    else:
        print("Error")

    return render(request,'users.html',{'form':form})
