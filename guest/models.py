from django.db import models

# Create your models here.
class Guest(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    date_of_birth = models.CharField(max_length=10)  # 1998/01/01
    sex = models.CharField(max_length=1)    # F
    phone_num = models.CharField(max_length=13)     # 010-0000-0000
    e_mail = models.CharField(max_length=50)
    nation = models.CharField(max_length=20)    #Korea
    guest_class = models.CharField(max_length=10)   #silver
