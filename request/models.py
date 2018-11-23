from django.db import models

# Create your models here.
class Request(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    guest_id = models.IntegerField(max_length=10)   #123456
    dept_name = models.CharField(max_length=20) #frontoffice
    request_time = models.DateTimeField(default='')
    contents = models.CharField(max_length = 1000)
