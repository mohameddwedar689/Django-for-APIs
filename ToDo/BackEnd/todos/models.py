from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    # this method that provide a human readble name for each future model instace
    def __str__(self):
        return self.title