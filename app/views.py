from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import time, random
from .models import script_status, task
from .utils import my_background_function
# Create your views here.


class RunScript(View):
    def get(self, request, *args, **kwargs):
        
        script_status_obj = script_status.objects.all()        
        if not script_status_obj :
            script_status_obj = script_status.objects.create()
        else :
            script_status_obj = script_status_obj.first()

        if script_status_obj.run :
        
            data = {
                'message': 'The script is already running !',
                'status': 'success'
            }
            return JsonResponse(data)
        
        
        my_background_function()
        script_status_obj.run = True
        script_status_obj.save()
        
        data = {
            'message': 'Call Api to dowloads the videos!',
            'status': 'success'
        }
        return JsonResponse(data)