from django.contrib import admin

# Register your models here.
from .models import NewPaper,fetchinfo,conferencedata,Mkeyword

admin.site.register(NewPaper)
admin.site.register(fetchinfo)
admin.site.register(conferencedata)
admin.site.register(Mkeyword)

