from django.db import models

# Create your models here.

class products(models.Model):
    Name = models.CharField(unique=True,max_length=50)
    Category=models.CharField(max_length=50)
    Delivery_Time = models.IntegerField(default=0)
    Rating = models.FloatField(default=5.00)
    Stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    Sales_count=models.IntegerField(default=0)



# ID    Integer
# Name_of_Item  String
# Item_Category String
# Delivery Time Integer
# Rating    Float
# Warehouse_Stock   Integer
# Price Integer
# Created_Timestamp Datetime
# Sales_count   Integer
