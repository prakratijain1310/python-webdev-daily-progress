from django.db import models

# Create your models here.
class Todo(models.Model):
    taskname=models.CharField(max_length=100)
    startdate=models.DateField()
    enddate=models.DateField()
    