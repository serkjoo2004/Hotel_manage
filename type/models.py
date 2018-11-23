from django.db import models
    
    # Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=10)  #sweet
    bed_type = models.CharField(max_length=10)  #twin
    capacity = models.IntegerField(max_length=10)   #2
    cost = models.IntegerField(max_length=10000000)
