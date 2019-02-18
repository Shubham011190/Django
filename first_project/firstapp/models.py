from django.db import models

class Topic(models.Model):
    topic_name=models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name

class WebPage(models.Model):
    topic= models.ForeignKey('Topic',on_delete=models.PROTECT)
    name= models.CharField(max_length=264, unique=True)
    url= models.URLField(unique=True)

    def __str__(self):
        return self.name



# Create your models here.
