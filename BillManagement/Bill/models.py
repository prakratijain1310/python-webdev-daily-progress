from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bills')
    productname = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.IntegerField()

    def __str__(self):
        return self.productname
