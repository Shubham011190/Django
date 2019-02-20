from django.db import models
class Name(models.Model):
    name=models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.name

class Data(models.Model):
    name=models.ForeignKey('Name',on_delete=models.PROTECT)
    url=models.URLField(unique=True)
    date=models.DateField()

    def __str__(self):
        return str(self.date)


# Create your models here.
