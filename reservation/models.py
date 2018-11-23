from django.db import models

# Create your models here.
class Reservation(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    room_num = models.IntegerField(max_length=10)
    guest_id = models.IntegerField(max_length=10)
    reserve_num = models.IntegerField(max_length=10)
    cost = models.IntegerField(max_length=100000000)
    date_start = models.DateTimeField(default='')
    date_end = models.DateTimeField(default='')
    book_time = models.DateTimeField(default='')
    companion = models.IntegerField(max_length=10)
