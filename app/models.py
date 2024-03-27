from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
        
class task(TimeStampModel):
    link = models.TextField(default='')
    thread = models.IntegerField(default=10)
    target = models.IntegerField(default=1000)
    views = models.IntegerField(default=0)
    completed = models.BooleanField(default = False)
    
    def save(self, *args, **kwargs):
        if self.views >= self.target:
            self.completed = True
        super(task, self).save(*args, **kwargs)
    
class script_status(TimeStampModel):
    run = models.BooleanField(default=False)
    