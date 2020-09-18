from django.db import models

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateField()
    stock = models.IntegerField()
    daily_rate = models.FloatField()
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
