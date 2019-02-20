from django.contrib import admin
from firstapp.models import Topic,WebPage,AccessRecord

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)

# Register your models here.
