from django.db import models

# Create your models here.
class Staff(models.Model):
    # ID
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    work_start_time = models.CharField(max_length=20)   # 11/21 09:00
    work_end_time = models.CharField(max_length=20) # 11/21 18:00
    work_weekday = models.CharField(max_length=3)   # 월요일
    date_of_birth = models.CharField(max_length=10)  # 1998/01/01
    sex = models.CharField(max_length=1)    # F
    status = models.IntegerField()  # 0 : not working, 1 : working
    phone_num = models.CharField(max_length=13)     # 010-0000-0000
    # photo = models.FileField(upload_to=path)
    # dept = models.ForeignKey(Department, on_delete=models.CASCADE)  # it needs to check whethere it is foreign key
