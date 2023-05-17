from django.db import models




class Stock(models.Model):
    Total_Stock  = models.CharField(max_length = 10)
    Total_Sales = models.CharField(max_length=10) 
    Profit = models.CharField(max_length=10)
    Loss = models.CharField(max_length=10)
    New_Order = models.TextField(max_length=100)
    
    
    