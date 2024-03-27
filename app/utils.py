
from django.http import HttpResponse
from django.shortcuts import render
from .decorators import background_task
import concurrent.futures, random
from .models import script_status, task
from django.db import models
from .bot import scrapping_bot
import time, threading

num_threads = 1
lines = []

def add_view_count(model_instance):
    if not isinstance(model_instance, models.Model):
        raise ValueError("Argument must be a Django model object")
    
    model_instance.views += 1
    model_instance.save()

def get_random_prx():
    global lines
    if not lines : 
        with open('proxy-data-for-keywordlit-test.txt', 'r') as file: lines = file.readlines()
        
    if lines :
        return random.choice(lines)
    else :
        with open('proxy-data-for-keywordlit-test.txt', 'r') as file: lines = file.readlines()
        return random.choice(lines)

def work():
    print('work function !')

def main():
    
    active_threads = set()

    def start_new_thread():
        while True:
            work(get_random_prx())
    
    # Start the initial threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(num_threads):
            future = executor.submit(start_new_thread)
            active_threads.add(future)

        # Monitor and replace completed threads
        while True:
            completed = concurrent.futures.wait(active_threads, return_when=concurrent.futures.FIRST_COMPLETED).done
            for thread in completed:
                active_threads.remove(thread)
                new_thread = executor.submit(start_new_thread)
                active_threads.add(new_thread)

def main2():
    active_threads = set()
    
    obj_task_li = [ i for i in task.objects.all() if i.completed == False]
    if not obj_task_li :
        time.sleep(10)
        return
    
    def process_task(obj_task):
        bt = scrapping_bot()
        for obj_task in obj_task_li:
            if bt.work(obj_task.link):
                add_view_count(obj_task)
    
    threads = []
    for obj_task in obj_task_li:
        for i in range(obj_task.thread):
            thread = threading.Thread(target=process_task, args=(obj_task,))
            threads.append(thread)
            thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

@background_task
def my_background_function():
    obj = script_status.objects.first()
    obj.run = True
    obj.save()
    try :
        while True :
            main2()
    except Exception as e:
        print(e)
    obj.run = False
    obj.save()
        