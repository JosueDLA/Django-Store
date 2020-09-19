from django.db import models
from django.utils import timezone

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    entry_date = models.DateField()
    stock = models.IntegerField()
    price = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
