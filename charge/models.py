from django.db import models
# Create your models here.
class Charge(models.Model):
    room_num = models.IntegerField(max_length=10)   #101
    staff_id = models.IntegerField(max_length=10)   #123456
