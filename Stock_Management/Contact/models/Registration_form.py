from django.db import models




class registration(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Mobile_No = models.IntegerField(default='0')
    Password = models.CharField(max_length=30)
    Confirm_password = models.CharField(max_length=30)