from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import time, random
from .models import script_status, task
from .utils import my_background_function
# Create your views here.

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class RunScript(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
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

class fetch_view_count(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        tasks = task.objects.all()
        status=tasks[0].completed
        views_completed=tasks[0].views
        target_views=tasks[0].target 
        thread=tasks[0].thread 
        video_link=tasks[0].link      
        
        return JsonResponse({'Task Data':{
            'completed':status,
            'views_completed':views_completed,
            'target_views':target_views,
            'thread':thread,
            'video_link':video_link}})