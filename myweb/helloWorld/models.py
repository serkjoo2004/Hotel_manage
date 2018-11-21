from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length = 10)
    address = models.CharField(max_length = 15)
    age = models.IntegerField(default = 15)
    introduction = models.TextField()

    def __str__(self):
        return self.name