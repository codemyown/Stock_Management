from django.db import models



class Login(models.Model):
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.Email