from django.urls import path
from django.conf.urls import include
from .views import *

urlpatterns = [
    path('run-script/',RunScript.as_view(),name='RunScript'),
    path('task-status/',fetch_view_count.as_view(),name='fetch_view_count'),

    path('create-request/',create_task.as_view(),name='create_task'),
    path('request-status/',view_task.as_view(),name='view_task'),
]