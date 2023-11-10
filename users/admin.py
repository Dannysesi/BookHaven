from django.contrib import admin
from .models import *
from books.admin import admin_site
# Register your models here.
admin_site.register(Profile)