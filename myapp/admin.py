from django.contrib import admin
from myapp.models import Topic,Access_Records,Webpage
# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Access_Records)
