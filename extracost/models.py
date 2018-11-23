from django.db import models

# Create your models here.
class ExtraCost(models.Model):
    reserve_num = models.IntegerField(max_length=20)    #12345
    total_cost = models.IntegerField(max_length=10000000)   #100000
    payment_type = models.CharField(max_length=20)  #creditcard
