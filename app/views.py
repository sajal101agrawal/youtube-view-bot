from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import time, random
from .models import script_status, task
from .utils import my_background_function
from rest_framework.views import APIView
# Create your views here.

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def generate_random_string(length=10):
    import random, string
    # Define the characters you want to include in the random string
    characters = string.ascii_letters 

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string


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
    


class create_task(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        if not 'url' in request.data or not request.data.get('url'):
            return JsonResponse({'Message':'url field not provided'}, status=400)
        url=request.data.get('url')

        if not 'view_count' in request.data or not request.data.get('view_count'):
            return JsonResponse({'Message':'view_count field not provided'}, status=400)
        view_target=request.data.get('view_count')
        view_target = int(view_target)

        if not 'thread' in request.data or not request.data.get('thread'):
            return JsonResponse({'Message':'thread field not provided'}, status=400)
        thread=request.data.get('thread')

        uniq_request_id=generate_random_string()

        print({'url':url,
         'view':view_target,
         'thread':thread})

        task.objects.create(
            link = url,
            thread = thread,
            target = view_target,
            request_id=uniq_request_id
        )

# ---------------------------This Block will Re-Run the Script ---------------------------------------------------------------
        script_status_obj = script_status.objects.all()        
        if not script_status_obj :
            script_status_obj = script_status.objects.create()
        else :
            script_status_obj = script_status_obj.first()     

        my_background_function()
        script_status_obj.run = True
        script_status_obj.save()
# ---------------------------This Block will Re-Run the Script ---------------------------------------------------------------

        return JsonResponse({'Message':'Task Created Successfully','request_id': uniq_request_id, 'status':201})
        # tasks = task.objects.all()
        # status=tasks[0].completed
        # views_completed=tasks[0].views
        # target_views=tasks[0].target 
        # thread=tasks[0].thread 
        # video_link=tasks[0].link      
        
        # return JsonResponse({'Task Data':{
        #     'completed':status,
        #     'views_completed':views_completed,
        #     'target_views':target_views,
        #     'thread':thread,
        #     'video_link':video_link}})
    
class view_task(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not 'request_id' in request.data or not request.data.get('request_id'):
            return JsonResponse({'Message':'request_id field not provided'}, status=400)
        request_id=request.data.get('request_id')

        tasks = task.objects.filter(request_id=request_id).first()

        if not tasks:
            return JsonResponse({'Message': 'Task not found'}, status=404)
        status=tasks.completed
        views_completed=tasks.views
        target_views=tasks.target 
        # thread=tasks.thread 
        video_link=tasks.link 

        
        return JsonResponse({'Task Data':{
            'completed':status,
            'views_completed':views_completed,
            'target_views':target_views,
            # 'thread':thread,
            'video_link':video_link}})
    


