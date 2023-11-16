from django.contrib import admin
from .models import Restaurant
from .models import CurrentLocation

admin.site.register(Restaurant)
admin.site.register(CurrentLocation)