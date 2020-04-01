from django.db import models
from django.utils import timezone



class Post(models.Model):    
    author = models.CharField(max_length=30)
    text = models.TextField()
    
    created_date = models.DateTimeField(
            default=timezone.now)


    def publish(self):
        self.save()
