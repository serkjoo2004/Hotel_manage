from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=20)  #front office
    role = models.CharField(max_length=20)  #receptionist
    tele_num = models.CharField(max_length=20)     # 010-0000-0000
