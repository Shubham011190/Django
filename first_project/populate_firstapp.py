import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

import random
from firstapp.models import Topic,WebPage,AccessRecord
from faker import Faker

fakegen= Faker()
topics_name=['Social','Gaming','WebSite','News']

def addTopic():
    t=Topic.objects.get_or_create(topic_name=random.choice(topics_name))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top=addTopic()

        fakeName=fakegen.company()
        fakeUrl=fakegen.url()
        fakeDate=fakegen.date()

        webpg=WebPage.objects.get_or_create(topic=top, name=fakeName,url=fakeUrl)[0]
        accessRec=AccessRecord.objects.get_or_create(name=fakeName,date=fakeDate)[0]

if __name__=='__main__':
    print('Populating !')
    populate(30)
    print('Population Complete!!')
