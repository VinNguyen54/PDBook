from tracemalloc import Statistic
from django.contrib import admin
from .models import User, Statistics
# Register your models here.

admin.site.register(User)
admin.site.register(Statistics)
