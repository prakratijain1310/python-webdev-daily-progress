from django.db import models

# Create your models here.
class product_details(models.Model):
    productname=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    discount=models.IntegerField()
    