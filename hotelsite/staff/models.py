from django.db import models

class Room(models.Model): 
 
    TYPE_IN_CHOICES=(
        ('SINGLE', 'Single'),
        ('DOUBLE', 'Double'),
        ('SUITE', 'Suite')
    )
    
    STATUS_CLEAN_IN_CHOICES=(
        ('CLEAN', 'Clean'),
        ('UNCLEAN', 'Unclean')
    )
    room_num = models.DecimalField(decimal_places=0, max_digits=4, primary_key = 'True') 
    room_type = models.CharField(max_length=10, choices=TYPE_IN_CHOICES, default = 'SINGLE') #Suite 
    status_clean = models.CharField(max_length=10, choices=STATUS_CLEAN_IN_CHOICES, default='CLEAN')  # 0 : 사용중, 1 : 사용가능, 3 : 청소 필요, 4 : 예약
    
class Request_post(models.Model): 
    #요청번호는 자체 제공하는 pk이용 
    author =  models.ForeignKey('auth.User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=200) 
    text = models.TextField() 
    created_date = models.DateTimeField(default=timezone.now) 
    dept = models.ForeignKey('Department',on_delete=models.CASCADE, blank = True, null=True) 
    room_num = models.ForeignKey('Room', on_delete=models.CASCADE, blank = True, null = True) 

    def __str__(self): 
        return self.title 

class Department(models.Model): 
    name = models.CharField(max_length = 20) 
    role = models.TextField() 
    tel_num = models.CharField(max_length = 8) 

    def __str__(self): 
        return self.name 