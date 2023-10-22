from django.contrib import admin
from .models import CustomPerson, Team


admin.site.register(CustomPerson)
admin.site.register(Team)