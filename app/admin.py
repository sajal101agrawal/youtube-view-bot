from django.contrib import admin
from .models import task, script_status
# Register your models here.

admin.site.register(task)
admin.site.register(script_status)
