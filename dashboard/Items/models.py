from django.db import models
from django.contrib.auth.models import User

class Itemlist(models.Model):
    SKU = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Tags = models.CharField(max_length=10)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    In_stock = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    Available_stock = models.DecimalField(max_digits=5,decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=100)