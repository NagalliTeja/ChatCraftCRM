from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_ID = models.AutoField(primary_key=True)
    PRODUCT_NAME = models.CharField(max_length=35)
    UOM = models.CharField(max_length=35)
    QUANTITY_ON_HAND = models.IntegerField(default = 0)
    COST = models.IntegerField(default = 0)
    STATUS = models.CharField(max_length=35)