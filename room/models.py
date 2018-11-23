from django.db import models

# Create your models here.
class Room(models.Model):
    room_num = models.IntegerField(max_length=10)
    type = models.CharField(max_length=10)  #Sweet
    status = models.IntegerField(max_length=10)  # 0 : not working, 1 : workings
    items = models.IntegerField(max_length=100)  #아이템 종류별로 코드번호 붙여서 표시
