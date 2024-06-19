from django.contrib import admin
from .models import User, Record
# Register your models here.

#register user and record models
admin.site.register(User)
admin.site.register(Record)