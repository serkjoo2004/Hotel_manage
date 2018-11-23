from django.db import models

# Create your models here.
class GuestCar(models.Model):
    guest_id = models.IntegerField(max_length=10)   #123456
    car_num = models.IntegerField(max_length=10)
