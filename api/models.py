from django.db import models
from django.forms import CharField

# Create your models here.
class Todo(models.Model):
     title = models.CharField(max_length=100)
     description = models.CharField(max_length=500,blank=True)
     completed = models.BooleanField(default=False,blank=True,null=True)
     addedTime = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return (self.title)