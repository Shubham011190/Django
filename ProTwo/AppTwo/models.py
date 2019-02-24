from django.db import models

class User(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    email= models.EmailField(max_length=264,unique=True)

# Create your models here.
