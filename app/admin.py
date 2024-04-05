from django.contrib import admin
from .models import task, script_status
from .models import *
# Register your models here.


class taskAdmin(admin.ModelAdmin):
    list_display = ['id','views','completed','created','updated']


admin.site.register(task,taskAdmin)
admin.site.register(script_status)
