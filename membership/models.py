from django.db import models

# Create your models here.
class Membership(models.Model):
    membership_class = models.CharField(max_length=10)  #silver
    discount = models.IntegerField(max_length=100)
    cumulative_cost = models.IntegerField(max_length=10000000)  #100000
    reserve_count = models.IntegerField(max_length=100) #10

