from django.contrib import admin
from my_app1.models import Musician,Album

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)