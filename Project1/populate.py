import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from firstapp.models import Name,Data
from faker import Faker

fakegen=Faker()
names=['Shubham','Singhal','Sam','Raj']

def addName():
    n=Name.objects.get_or_create(name=random.choice(names))[0]
    return n

def population(N=3):
    for entry in range(N):
        name1=addName()

        fakeUrl=fakegen.url()
        fakeDate=fakegen.date()

        data=Data.objects.get_or_create(name=name1,url=fakeUrl,date=fakeDate)[0]

if __name__=='__main__':
    print('Populaing!')
    population(20)
    print('Population Complete')
