from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ReceptionistInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    middle_name=models.CharField(max_length=15)
    age = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    region=models.CharField(max_length=20)
    zone=models.CharField(max_length=20)
    woreda=models.CharField(max_length=20)
    kebele=models.CharField(max_length=20)
    house_no=models.CharField(max_length=20)
    def __str__(self): 
        return self.user.username