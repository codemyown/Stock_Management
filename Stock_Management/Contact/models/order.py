from django.db import models




class Order(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Order = models.CharField(max_length=200)
    Address = models.CharField(max_length=150)
    Query = models.TextField()
    